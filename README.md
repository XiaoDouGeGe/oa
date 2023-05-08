# oa

## 代码
### frontend - 前端代码  
### backend  - 后端代码
### conf     - 配置文件  
---

## 部署
docker run -p 18080:8080 -p 15432:5432 -p 18880:80 --privileged=true --name <oa06> --hostname hostoa -itd <oa:0.6> /usr/sbin/init

