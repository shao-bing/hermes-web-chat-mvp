# hermes-web-chat-mvp

## 浏览器 → Hermes → DeepSeek，这是整个Hermes最轻量的一层。
##  整个链路非常简单。前提：需要先自己安装好 Hermes egent ，准备好 deepseek key 。
### 整体结构如下：
``` text
Browser

     │

     ▼

index.html

     │

fetch()

     │

     ▼

FastAPI

     │

DeepSeek SDK

     │

     ▼

DeepSeek API

     │

返回答案

     │

     ▼

Browser
```

##建立目录
``` text
hermes-web-chat-mvp/

├── frontend/

│   └── index.html

│

├── backend/

│   ├── app/

│   │

│   ├── main.py

│   │

│   ├── chat.py

│   │

│   └── requirements.txt

│

└── README.md
```

### more details: https://happyrock.cloud/docs/hermes-web-chat-mvp/

