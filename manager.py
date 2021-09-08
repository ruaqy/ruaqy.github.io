import os, re, time, json, uuid, logging


class WebManager:
    def __init__(self):
        # 打开数据库
        data_name = './data/dt.json'
        if os.path.isfile(data_name):
            with open(data_name, encoding="utf-8") as dt:
                self.web_dt = json.load(dt)
                logging.info("Database Existed, Readed.")
        else:
            self.web_dt = {}
            logging.info("Database Does Not Exist, Created.")
    
    def __del__(self):
        # 退出前保存
        # self.save()
        pass
    
    # 保存数据库    
    def save(self):
        data_name = './data/dt.json'
        with open(data_name, 'w', encoding="utf-8") as dt:
            json.dump(self.web_dt, dt)
        logging.info("Database Parser Completed.")


    # 根据文件编译数据库
    def parser_data(self):
        # 读取文章写入数据库
        def read_article():
            files = os.listdir('./pages/post/')
            articles = []
            for out_file in files:
                # 获得文件修改时间
                filemt= time.strftime('%Y-%m-%d', time.localtime(os.stat("./pages/post/{}".format(out_file)).st_mtime))
                title, main_text = "", ""
                with open("./pages/post/{}".format(out_file), encoding="utf-8") as article:
                    title = article.readline()
                    title = re.match("# (.+)", title)
                    if title:
                        title = title.group(1)
                    else:
                        logging.warn("Not match title, post:{}".format(out_file))                    
                    main_text = article.read(60)
                    if main_text:
                        main_text = re.sub(r'\s+', '', main_text)
                    else:
                        logging.warn("Not match text, post:{}".format(out_file))                    
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
                post = self.web_dt.get("article", [])[-1]
                append_text = """---
### [{}](./post.html#pages/post/{})

{}

**{}**
    
""".format(post.get("title", ""), post.get("url", ""), post.get("main", ""), post.get("time", ""))
                recent_post += append_text
                
                recent_proj = '## 近期项目\n'
                proj = self.web_dt.get("proj", [])[-1]
                recent_proj += "\n"+proj.get("url", "")+"\n"
                
                f.write(out_text + recent_post + recent_proj)
                
        def write_article():
            out_text = '# 文章\n'
            with open("pages/article.md", 'w', encoding="utf-8") as f:
                # 获取数据
                for item in self.web_dt.get("article", []):
                    append_text = """---
### [{}](./post.html#pages/post/{})

{}

**{}**
    
""".format(item.get("title", ""), item.get("url", ""), item.get("main", ""), item.get("time", ""))
                    out_text += append_text
                logging.info("Article Publish Completed.")
                f.write(out_text)
                
        def write_project():
            out_text = '# 项目\n'
            with open("pages/project.md", 'w', encoding="utf-8") as f:
                # 获取数据
                for item in self.web_dt.get("proj", []):
                    append_text = item.get("url")
                    out_text += "\n" + append_text + "\n"
                logging.info("Project Publish Completed.")
                f.write(out_text)
    
        write_home()
        write_article()
        write_project()
        
    def add_proj(self, proj):
        proj_ls = self.web_dt.get("proj", [])
        uid = uuid.uuid3(uuid.NAMESPACE_DNS, proj)
        proj_ls.append({"url":proj, "id": str(uid)})
        self.web_dt["proj"] = proj_ls
        logging.info("Project Has Log.Uuid:{}".format(uid))
        
    
if __name__ == '__main__':
    # 启动日志
    logging.basicConfig(level=logging.DEBUG)
    
    manager = WebManager()
    manager.parser_data()

    
    manager.add_proj(r"[![RQY/RuaBlog](https://gitee.com/muronglengjing/rua-blog/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/rua-blog)")
    manager.add_proj(r"[![RQY/ST7735S LCD驱动](https://gitee.com/muronglengjing/st7735-s-lcd-driver/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/st7735-s-lcd-driver)")
    manager.add_proj(r"[![RQY/学生信息管理系统](https://gitee.com/muronglengjing/my_student_manager/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/my_student_manager)")
    manager.add_proj(r"[![RQY/DjangoOnlineShop](https://gitee.com/muronglengjing/django-online-shop/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/django-online-shop)")
    
    
    manager.connect_file()
    
    manager.save()
