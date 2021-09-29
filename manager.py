import os, re, sys, time, json, shutil, getopt, logging


class SiteManager:
    def __init__(self, state):
        # 打开数据库
        # dt_arti.json文章数据库
        # dt_proj.json项目数据库
        # dt_home.json首页数据库
        self.state = state
        
        urls = ['./data/dt_arti.json', './data/dt_proj.json', 
                './data/dt_home.json' ]
        state = ["A", "P", "H"]
        
        if self.state in state:
            self.data_name = urls[state.index(self.state)]
            
        if os.path.isfile(self.data_name):
            with open(self.data_name, encoding="utf-8") as dt:
                self.web_dt = json.load(dt)
                logging.debug("数据库存在,加载中.")
        else:
            self.web_dt = {}
            logging.debug("数据库不存在,已创建.")
            
    def save(self):
        with open(self.data_name, 'w', encoding="utf-8") as dt:
            json.dump(self.web_dt, dt)
            print(self.web_dt)
            
        logging.debug("数据库已保存.")
        
    # 根据文件编译数据库
    def parser_data(self):
        # 读取文章写入数据库
        def read_article():
            files = os.listdir(r'./pages/post/')
            # 文章数据
            articles = []
            for out_file in files:
                # 创建时间
                ctime = os.stat("./pages/post/{}".format(out_file)).st_ctime
                # 修改时间
                mtime = os.stat("./pages/post/{}".format(out_file)).st_mtime
                
                # filemt= time.strftime('%Y-%m-%d', time.localtime())
                
                # 标题 概要
                title, main_text = "", ""
                with open("./pages/post/{}".format(out_file), encoding="utf-8") as article:
                    # 读取标题
                    title = article.readline()
                    title = re.match("#+ (.+)", title)
                    
                    if title:
                        title = title.group(1)
                    else:
                        logging.warning("无标题:{}".format(out_file))                    
                    main_text = article.read(60)
                    
                    if main_text:
                        main_text = re.sub(r'\s+', '', main_text)
                    else:
                        logging.warning("无正文:{}".format(out_file))       
                        
                    logging.debug("文本解析完成:{}".format(out_file))
                    
                    # | t_t  | 文章标题 |
                    # | m_c  | 文章概览 |
                    # | c_t  | 创建时间 |
                    # | m_t  | 修改时间 |
                    # | url  | 文章地址 |
                    
                    articles.append({"t_t": title, 
                                     "m_c":main_text,
                                     "c_t":ctime,
                                     "m_t":mtime,
                                     "url":"./post.html#pages/post/{}".format(out_file)})
                    
            articles = sorted(articles, key=lambda x:x.get("c_t", 0), reverse=True)
            
            
            
            for article in articles:
                article["c_t"] = time.strftime('%Y-%m-%d', time.localtime(article.get("c_t", 0)))
                article["m_t"] = time.strftime('%Y-%m-%d', time.localtime(article.get("m_t", 0)))
            
            # 重建数据库
            self.web_dt["article"] = articles 
    
        if self.state == "A":
            read_article()
            
    def move_draft(self):
        # 移动草稿
        def read_draft():
            path = r'./pages/draft/'
            path_target = r"./pages/post/"
            files = os.listdir(path)
            if not files:
                logging.warning("Is no draft to post.")
            else:
                print("Index", "File Name", "Create Time", sep='\t')
                for f_index in range(len(files)):
                    out_file = files[f_index]
                    # 获得文件修改时间
                    filemt= time.strftime('%Y-%m-%d', time.localtime(os.stat(path+out_file).st_ctime))
                    print(f_index, out_file, filemt, sep='\t')
                f_index = input("Please press number of which you want to post.")
                if f_index.isnumeric():
                    s_file = path + files[int(f_index)]
                    t_file = path_target + files[int(f_index)]
                    shutil.move(s_file, t_file)
                    logging.info("Draft posted:{}.".format(files[int(f_index)])) 
                else:
                    logging.error("Please input the number.")            
        read_draft()
        
    def add_proj(self):
        proj_ls = self.web_dt.get("project", [])
        t_t = input("请输入项目标题")
        m_c = input("请输入项目概览")
        p_s = input("请输入项目状态")
        p_l = input("请输入项目链接")
        p_p = input("请输入项目备注")
        proj_ls.append({"t_t": t_t, "m_c": m_c, "p_s": p_s, "p_l": p_l, "p_p": p_p})
        self.web_dt["project"] = proj_ls
    
    def remove_proj(self):
        proj_ls = self.web_dt.get("project", [])
        # | t_t  | 项目标题 |
        # | m_c  | 项目概览 |
        # | p_s  | 项目状态 |
        # | p_l  | 项目链接 |
        # | p_p  | 项目备注 |
        t_t = input("请输入项目标题")
        m_c = input("请输入项目概览")
        p_s = input("请输入项目状态")
        p_l = input("请输入项目链接")
        p_p = input("请输入项目备注")
        proj_ls.append({"t_t": t_t, "m_c": m_c, "p_s": p_s, "p_l": p_l, "p_p": p_p})
        print(proj_ls)
        print(123)
        self.web_dt["project"] = proj_ls
    
    
def main(argv):
    if not argv:
        # 输入指令为空
        print("Please input the command.Press -h or -help to get help.")
        sys.exit(0)
    
    try:
        opts, args = getopt.getopt(argv,"a:rmpbgh",["help", "remove","add=",
                                                   "move","parser","build",
                                                   "generate", "pa"])
    except getopt.GetoptError:
        logging.error("Command error.Press -h or -help to get help.")
        sys.exit(1)
        
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            # 帮助文件
            print("""
用法: python manager.py [option] [arg] ...
选项 与 变量:
    -a or --add      : 添加文章
                       -a [文章名]
                       --add [文章名]
                       文章名不是一个可选项
    -r or --remove   : remove the project of web site.
    
    
    
    -c or --create   : write markdown draft.
    -m or --move     : move the draft to post.
    -d or --delete   : move the post to draft(delete post).
    
    -p or --parser   : parser the database.
    -b or --build    : bulid the markdown file.
    -g or --generate : generate the database and the markdown file.

    --pa           :添加项目 

              """)
            sys.exit(0)
            
        if opt in ('-a', "--add"):
            manager = SiteManager("P")

            manager.add_proj(arg)
            manager.save()
            sys.exit(0)
                    
        if opt in ('-r', "--remove"):
            manager = SiteManager("P")

            
            manager.remove_proj()
            manager.save()
            sys.exit(0)
    
        if opt in ('-m', "--move"):
            manager.move_draft()
            sys.exit(0)
            
        if opt in ('-p', "--parser"):
            manager = SiteManager("A")
            
            manager.parser_data()
            manager.save()
            sys.exit(0)
            
        if opt in ('-b', "--build"):
            manager = SiteManager("P")
            
            sys.exit(0)
            
        if opt in ('-g', "--generate"):
            manager = SiteManager("P")
            
            manager.parser_data()
            manager.save()
            sys.exit(0)
            
        if opt in ("--pa"):
            manager = SiteManager("P")
            
            manager.add_proj()
            manager.save()
            sys.exit(0)
   

if __name__ == '__main__':
    
    # 启动日志
    logging.basicConfig(level=logging.DEBUG)
    
    main(sys.argv[1:])



