import os, re, sys, time, json, shutil, getopt, logging


class WebManager:
    def __init__(self):
        # 打开数据库
        data_name = './data/dt.json'
        if os.path.isfile(data_name):
            with open(data_name, encoding="utf-8") as dt:
                self.web_dt = json.load(dt)
                logging.debug("Database existed, readed.")
        else:
            self.web_dt = {}
            logging.debug("Database does not exist, created.")
    
    def __del__(self):
        # 退出前保存
        # self.save()
        pass
    
    # 保存数据库    
    def save(self):
        data_name = r'./data/dt.json'
        with open(data_name, 'w', encoding="utf-8") as dt:
            json.dump(self.web_dt, dt)
        logging.debug("Database parser completed.")


    # 根据文件编译数据库
    def parser_data(self):
        # 读取文章写入数据库
        def read_article():
            files = os.listdir(r'./pages/post/')
            articles = []
            for out_file in files:
                # 获得文件修改时间
                filemt= time.strftime('%Y-%m-%d', time.localtime(os.stat("./pages/post/{}".format(out_file)).st_ctime))
                title, main_text = "", ""
                with open("./pages/post/{}".format(out_file), encoding="utf-8") as article:
                    title = article.readline()
                    title = re.match("#+ (.+)", title)
                    if title:
                        title = title.group(1)
                    else:
                        logging.warning("Not match title, post:{}".format(out_file))                    
                    main_text = article.read(60)
                    if main_text:
                        main_text = re.sub(r'\s+', '', main_text)
                    else:
                        logging.warning("Not match text, post:{}".format(out_file))                    
                    logging.debug("Parser text finished:{}".format(out_file))
                    
                    articles.append({"title": title, 
                                     "url":out_file,
                                     "main":main_text,
                                     "time":filemt})
            self.web_dt["article"] = articles
        read_article()
        
    def connect_file(self):
        def write_home():
            # 生成文章页
            out_text = '# 主页\n\n'
            with open("pages/home.md", 'w', encoding="utf-8") as f:
                recent_post = '## 近期文章\n'
                post = self.web_dt.get("article", [])
                if post:
                    append_text = """---
### [{}](./post.html#pages/post/{})

{}

**{}**
    
""".format(post[-1].get("title", ""), post[-1].get("url", ""), post[-1].get("main", ""), post[-1].get("time", ""))
                recent_post += append_text
                
                recent_proj = '## 近期项目\n'
                proj = self.web_dt.get("proj", [])
                if proj:
                    recent_proj += "\n"+proj[-1]+"\n"
                
                f.write(out_text + recent_post + recent_proj)
            
            logging.debug("Home Publish Completed.")
                
        def write_article():
            out_text = '# 文章\n'
            with open("pages/article.md", 'w', encoding="utf-8") as f:
                # 获取数据
                articles = self.web_dt.get("article", [])
                # 倒序输出
                for index in range(len(articles)-1, -1, -1):
                    item = articles[index]
                    append_text = """---
### [{}](./post.html#pages/post/{})

{}

**{}**
    
""".format(item.get("title", ""), item.get("url", ""), item.get("main", ""), item.get("time", ""))
                    out_text += append_text
                logging.debug("Article Publish Completed.")
                f.write(out_text)
                
        def write_project():
            out_text = '# 项目\n'
            with open("pages/project.md", 'w', encoding="utf-8") as f:
                # 获取数据
                for item in self.web_dt.get("proj", []):
                    out_text += "\n" + item + "\n"
                logging.debug("Project Publish Completed.")
                f.write(out_text)
    
        write_home()
        write_article()
        write_project()
        
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
        
    def add_proj(self, proj):
        proj_ls = self.web_dt.get("proj", [])
        if proj in proj_ls:
            logging.info("Project really exist:{}".format(proj))
        else:
            proj_ls.append(proj)
            # self.web_dt["proj"] = proj_ls
            logging.info("Project Has Log:{}".format(proj))
    
    def remove_proj(self):
        proj_ls = self.web_dt.get("proj", [])
        if not proj_ls:
            logging.info("Project does not have any thing.")
            sys.exit(0)
        for index in range(len(proj_ls)):
            print(index, proj_ls[index])
        index = input("please press number of which you want to remove.")
        if index.isnumeric():
            proj_ls.pop(int(index))
            logging.info("Project remove finish.")
        else:
            logging.error("Please input the number")
    
def main(argv):
    if not argv:
        # 输入指令为空
        print("Please input the command.Press -h or -help to get help.")
        sys.exit(0)
    
    try:
        opts, args = getopt.getopt(argv,"a:rmpbgh",["help", "remove","add=",
                                                   "move","parser","build",
                                                   "generate"])
    except getopt.GetoptError:
        logging.error("Command error.Press -h or -help to get help.")
        sys.exit(1)

    manager = WebManager()

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            # 帮助文件
            print("""
usage: python manager.py [option] [arg] ...
Options and arguments:
    -a or --add      : add the project of web site.use:
                       -a arg
                       --add arg
                       you need to add arg to the command. 
    -r or --remove   : remove the project of web site.
    
    
    -c or --create   : write markdown draft.
    -m or --move     : move the draft to post.
    -d or --delete   : move the post to draft(delete post).
    
    -p or --parser   : parser the database.
    -b or --build    : bulid the markdown file.
    -g or --generate : generate the database and the markdown file.
                  """)
            sys.exit(0)
            
        if opt in ('-a', "--add"):
            manager.add_proj(arg)
            manager.save()
            sys.exit(0)
                    
        if opt in ('-r', "--remove"):
            manager.remove_proj()
            manager.save()
            sys.exit(0)
    
        if opt in ('-m', "--move"):
            manager.move_draft()
            sys.exit(0)
            
        if opt in ('-p', "--parser"):
            manager.parser_data()
            manager.save()
            sys.exit(0)
            
        if opt in ('-b', "--build"):
            manager.connect_file()
            sys.exit(0)
            
        if opt in ('-g', "--generate"):
            manager.parser_data()
            manager.connect_file()
            manager.save()
            sys.exit(0)
   

if __name__ == '__main__':
    
    # 启动日志
    logging.basicConfig(level=logging.DEBUG)
    
    main(sys.argv[1:])

