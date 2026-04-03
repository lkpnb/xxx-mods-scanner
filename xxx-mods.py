import os
import socket
import requests
import re

print("""\033[035m                                                                                                                                                                          
                                                                                                                                                                          
XXXXXXX       XXXXXXXXXXXXXX       XXXXXXXXXXXXXX       XXXXXXX                 MMMMMMMM               MMMMMMMM     OOOOOOOOO     DDDDDDDDDDDDD           SSSSSSSSSSSSSSS 
X:::::X       X:::::XX:::::X       X:::::XX:::::X       X:::::X                 M:::::::M             M:::::::M   OO:::::::::OO   D::::::::::::DDD      SS:::::::::::::::S
X:::::X       X:::::XX:::::X       X:::::XX:::::X       X:::::X                 M::::::::M           M::::::::M OO:::::::::::::OO D:::::::::::::::DD   S:::::SSSSSS::::::S
X::::::X     X::::::XX::::::X     X::::::XX::::::X     X::::::X                 M:::::::::M         M:::::::::MO:::::::OOO:::::::ODDD:::::DDDDD:::::D  S:::::S     SSSSSSS
XXX:::::X   X:::::XXXXXX:::::X   X:::::XXXXXX:::::X   X:::::XXX                 M::::::::::M       M::::::::::MO::::::O   O::::::O  D:::::D    D:::::D S:::::S            
   X:::::X X:::::X      X:::::X X:::::X      X:::::X X:::::X                    M:::::::::::M     M:::::::::::MO:::::O     O:::::O  D:::::D     D:::::DS:::::S            
    X:::::X:::::X        X:::::X:::::X        X:::::X:::::X                     M:::::::M::::M   M::::M:::::::MO:::::O     O:::::O  D:::::D     D:::::D S::::SSSS         
     X:::::::::X          X:::::::::X          X:::::::::X      --------------- M::::::M M::::M M::::M M::::::MO:::::O     O:::::O  D:::::D     D:::::D  SS::::::SSSSS    
     X:::::::::X          X:::::::::X          X:::::::::X      -:::::::::::::- M::::::M  M::::M::::M  M::::::MO:::::O     O:::::O  D:::::D     D:::::D    SSS::::::::SS  
    X:::::X:::::X        X:::::X:::::X        X:::::X:::::X     --------------- M::::::M   M:::::::M   M::::::MO:::::O     O:::::O  D:::::D     D:::::D       SSSSSS::::S 
   X:::::X X:::::X      X:::::X X:::::X      X:::::X X:::::X                    M::::::M    M:::::M    M::::::MO:::::O     O:::::O  D:::::D     D:::::D            S:::::S
XXX:::::X   X:::::XXXXXX:::::X   X:::::XXXXXX:::::X   X:::::XXX                 M::::::M     MMMMM     M::::::MO::::::O   O::::::O  D:::::D    D:::::D             S:::::S
X::::::X     X::::::XX::::::X     X::::::XX::::::X     X::::::X                 M::::::M               M::::::MO:::::::OOO:::::::ODDD:::::DDDDD:::::D  SSSSSSS     S:::::S
X:::::X       X:::::XX:::::X       X:::::XX:::::X       X:::::X                 M::::::M               M::::::M OO:::::::::::::OO D:::::::::::::::DD   S::::::SSSSSS:::::S
X:::::X       X:::::XX:::::X       X:::::XX:::::X       X:::::X                 M::::::M               M::::::M   OO:::::::::OO   D::::::::::::DDD     S:::::::::::::::SS 
XXXXXXX       XXXXXXXXXXXXXX       XXXXXXXXXXXXXX       XXXXXXX                 MMMMMMMM               MMMMMMMM     OOOOOOOOO     DDDDDDDDDDDDD         SSSSSSSSSSSSSSS\033[03m   
\033[034m[*]一款适合新手的信息收集工具
[*]by xxx\033[0m""")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
while True:
    print("\033[033m功能1：网站存活扫描\n"
          "功能2：子域名挖掘\n"
          "功能3：目录扫描\n"
          "功能4：指纹识别\n"
          "功能5：403绕过\033[0m")
    gongneng=input("\033[033m输入数字：\033[0m")
    if gongneng != "1" and gongneng != "2" and gongneng != "3" and gongneng != "4" and gongneng != "5":
        continue
    else:
        save_path="XXX-mods结果"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print(f"结果文件储存位置:{save_path}")
        else:
            print("储存文件已经存在")
        if gongneng=="1":
            lujing=input("请存储网站的txt文件地址(格式"文件地址"):")
            if '"' in lujing:
                lujing1=lujing.replace('"','')
                lujing2=lujing1.split(".")[0]
                with open(lujing,"r",encoding="utf-8") as f:
                    wangzhang=f.read().splitlines()
                    for a in wangzhang:
                        try:
                            if "http://" not in a and "https://" not in a:
                                url="http://"+a
                                response = requests.get(url,headers=headers,timeout=2.5)
                                response.encoding="utf-8"
                                title=re.findall(r"<title>(.*?)</title>",response.text)
                                pry=re.findall(r"\d+\.\d+\.\d+\.\d+",response.text)
                                print(f"目标网站：{a}  --> 状态码：{response.status_code}  -->标题：{title}  --> 可能存在代理{pry} ")
                                with open(f"XXX-mods结果/{lujing2}探活结果.txt","a+",encoding="utf-8") as f:
                                    f.write(f"目标网站：{a}  --> 状态码：{response.status_code}  -->标题：{title}  --> 可能存在代理{pry}\n")
                            else:
                                url=a
                                response = requests.get(url,headers=headers,timeout=2.5)
                                response.encoding="utf-8"
                                title=re.findall(r"<title>(.*?)</title>",response.text)
                                pry=re.findall(r"\d+\.\d+\.\d+\.\d+",response.text)
                                print(f"目标网站：{a}  --> 状态码：{response.status_code}  -->标题：{title}  --> 可能存在代理{pry} ")
                                with open(f"XXX-mods结果/{lujing2}探活结果.txt","a+",encoding="utf-8") as f:
                                    f.write(f"目标网站：{a}  --> 状态码：{response.status_code}  -->标题：{title}  --> 可能存在代理{pry}\n")
                        except Exception as e:
                            print(f"目标网站：{a}失活")


        # # response = requests.get(url, headers=headers)
        # # response.encoding='utf-8'
        # resuilt=socket.gethostbyname("www.hxxy.edu.cn")
        if gongneng=="2":
            url=input("输入网站（http或者https格式）:")
            print("正在执行")
            urls=url.replace(url.split('//')[0],'')
            with open(r"subdomains-top1million-20000.txt","r") as f:
                paths=f.read().splitlines()
                for i in paths:
                    try:
                        subdomain=i+url.replace(url.split('.')[0],"")
                        resuilt=socket.gethostbyname(subdomain)
                        with open(f"XXX-mods结果/{urls}子域名扫描结果.txt", "a+", encoding="utf-8") as f:
                            f.write(f"目标：{url}  子域名：{subdomain}   ip：{resuilt}\n")
                        print(f"子域名：{subdomain}  ip：{resuilt}")

                    except:
                        pass
        if gongneng=="3":
            url=input("输入网站（http或者https格式）:")
            print("正在执行(可能要比较久)")
            with open(r"dir.txt","r",encoding="utf-8") as f:
                    paths=f.read().splitlines()
                    for i in paths:
                        try:
                            tager_url=url+i
                            url1= url.replace("://", "")
                            url2 = url1.replace("http", "")
                            response=requests.get(tager_url,headers=headers,timeout=2.5)
                            response.encoding="utf-8"
                            title=re.findall(r"<title>(.*?)</title>",response.text)[0]
                            if response.status_code==200:
                                print(f"\033[032m网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->成功访问\033[0m")
                                with open(f"XXX-mods结果/{url2}目录扫描结果.txt","a+",encoding="utf-8") as f:
                                    f.write(f"网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->成功访问\n")
                            elif response.status_code==403:
                                print(f"\033[032m网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->403权限拒绝可能存在绕过\033[0m")
                                with open(f"XXX-mods结果/{url2}目录扫描结果.txt","a+",encoding="utf-8") as f:
                                    f.write(f"网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->403权限拒绝可能存在绕过\n")
                            elif response.status_code==301 or response.status_code==302:
                                print(f"\033[032m网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->可能存在跳转漏洞\033[0m")
                                with open(f"XXX-mods结果/{url2}目录扫描结果.txt","a+",encoding="utf-8") as f:
                                    f.write(f"网站：{tager_url}  --> 状态码：{response.status_code}  --> 标题：{title}  -->可能存在跳转漏洞\n")
                            else:
                                print(f"网站：{tager_url}目录不存在")
                        except Exception as e:
                            print(f"url:{tager_url}可能无法响应")
        if gongneng=="4":
            wangzhang1=input("输入识别网站(http或者https格式)：")
            wangzhangs=wangzhang1.replace("://","")
            wangzhangd=wangzhangs.replace("http","")
            try:
                requests.packages.urllib3.disable_warnings()
                response=requests.get(wangzhang1,headers=headers,timeout=15,allow_redirects=True,verify=False)
                print("========指纹识别结果========")
                print(f"网站:{wangzhang1} --> 状态码：{response.status_code}")
                print(f"Server:{response.headers.get('Server','无')}")
                print(f"框架:{response.headers.get('X-Powered-By','无')}")
                print(f"输出语言:{response.headers.get('Content-Type','无')}")
                with open(f"XXX-mods结果/{wangzhangd}指纹结果.txt", "a+", encoding="utf-8") as f:
                    f.write("========指纹识别结果========\n"
                            f"网站:{wangzhang1} --> 状态码：{response.status_code}\n"
                            f"Server:{response.headers.get('Server','无')}\n"
                            f"框架:{response.headers.get('X-Powered-By','无')}\n"
                            f"输出语言:{response.headers.get('Content-Type','无')}")

            except:
                print(f"网站：{wangzhang1}未响应")
        if gongneng=="5":
            wd=input("输入需要403绕过的网站（http或者https格式）:")
            requests.packages.urllib3.disable_warnings()
            head={"X-Forwarded-For":"127.0.0.1",
                  "X-Real-IP":"127.0.0.1",
                  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

            try:
                with open("403bypass.txt","r",encoding="utf-8") as f:
                    resuilts1=f.read().splitlines()
                    for i in resuilts1:
                        urls = wd.split("/")[-1]
                        url4 = i + urls
                        url5 = wd.replace(wd.split("/")[-1], "") + url4
                        response = requests.get(url5, headers=head, timeout=2.5, verify=False, allow_redirects=True)
                        title = re.findall(r"<title>(.*?)</title>", response.text)
                        if response.status_code == "200":
                            print(f"目标网站：{url5}  --> 状态码：{response.status_code}  -->绕过成功")
                            with open("XXX-mods结果/403绕过成功结果.txt", "a+", encoding="utf-8") as f:
                                f.write(f"\033[032m目标网站：{url5}  --> 状态码：{response.status_code}  -->绕过成功\n\033[0m")
                        else:
                            print(f"目标：{url5}绕过失败")
                    for i in resuilts1:
                        url=wd+i
                        response=requests.get(url,headers=head,timeout=2.5,verify=False,allow_redirects=True)
                        title = re.findall(r"<title>(.*?)</title>", response.text)
                        if response.status_code=="200":
                            print(f"目标网站：{url}  --> 状态码：{response.status_code}  -->绕过成功")
                            with open("XXX-mods结果/403绕过成功结果.txt","a+",encoding="utf-8") as f:
                                f.write(f"\033[032m目标网站：{url}  --> 状态码：{response.status_code}  -->绕过成功\n\033[0m")
                        else:
                            print(f"目标：{url}绕过失败")


            except Exception as e:
                print(f"{e}")









