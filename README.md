# wxbot_project_py2.7

目录结构:
```bash
.
├── README.md
├── config
│   ├── __init__.py
│   ├── config_manager.py
│   ├── constant.py
│   ├── log.py
│   ├── requirements.txt
│   └── wechat.conf.bak
├── db
│   ├── __init__.py
│   ├── mysql_db.py
│   └── sqlite_db.py
├── docker
│   ├── Dockerfile
│   └── README.md
├── server
│   ├── index.html
│   └── upload.html
├── tmp_data
├── wechat
│   ├── __init__.py
│   ├── utils.py
│   ├── wechat.py
│   ├── wechat_apis.py
│   └── wechat_js_backup
│       └── index_40649b7.js
├── weixin_bot.py
└── wx_handler
    ├── __init__.py
    ├── bot.py
    └── wechat_msg_processor.py
```
---
# 登录异常DEBUG
11:58 2017/6/3
<error><ret>1203</ret><message>当前登录环境异常。为了你的帐号安全，暂时不能登录web微信。你可以通过手机客户端或者windows微信登录。</message></error>

---
# 获得access_token

    ''''' 第一次使用,获得access_token
      AppId client_credentials
      API Key o0blfndGWGQq0PO0SzG50IZb
      Secret Key lKR0HCRB6VA3mu7QVAvtQ04ZD3upMZTF
      
      curl -i -k 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=o0blfndGWGQq0PO0SzG50IZb&client_secret=lKR0HCRB6VA3mu7QVAvtQ04ZD3upMZTF'
      
      {"access_token":"24.7c16b2c05db66bac04a2fd4abe403ca0.2592000.1499134465.282335-9723636","session_key":"9mzdDFYRLXDc7rWt5Grmo3YwY95UwVcDcb5kbXOilLMyYo3FXD7YdnVWAef7OOv8WIbksDrvrL6AtXYQ6rtQh5MTu0Xu","scope":"public vis-faceverify_faceverify vis-ocr_ocr vis-faceattribute_faceattribute nlp_simnet nlp_wordemb nlp_comtag nlp_dnnlm_cn vis-antiporn_antiporn_v2 brain_ocr_scope vis-faceverify_faceverify_v2 brain_gif_antiporn brain_ocr_general brain_ocr_general_basic vis-classify_terror brain_ocr_webimage brain_nlp_lexer brain_all_scope brain_ocr_idcard brain_antiporn brain_antiterror brain_nlp_comment_tag brain_nlp_dnnlm_cn brain_nlp_word_emb_vec brain_nlp_word_emb_sim brain_nlp_sentiment_classify audio_voice_assistant_get audio_tts_post wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian wangrantest_test wangrantest_test1 bnstest_test1 bnstest_test2 vis-classify_flower","refresh_token":"25.92621f4a82543df6cc0ea091af215800.315360000.1811902465.282335-9723636","session_secret":"afb09c3019379fdc8aaf90beef8086b4","expires_in":2592000}
      
      access_token 24.7c16b2c05db66bac04a2fd4abe403ca0.2592000.1499134465.282335-9723636
      
    '''
---
# access_token  api.baidubec

对比获得access_token
https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=o0blfndGWGQq0PO0SzG50IZb&client_secret=lKR0HCRB6VA3mu7QVAvtQ04ZD3upMZTF'
https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=o0blfndGWGQq0PO0SzG50IZb&client_secret=lKR0HCRB6VA3mu7QVAvtQ04ZD3upMZTF'

2017-06-04 14:21:50,478 - requests.packages.urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): aip.baidubce.com
2017-06-04 14:21:50,991 - requests.packages.urllib3.connectionpool - DEBUG - https://aip.baidubce.com:443 "GET /oauth/2.0/token?client_secret=lKR0HCRB6VA3mu7QVAvtQ04ZD3upMZTF&grant_type=client_credentials&client_id=o0blfndGWGQq0PO0SzG50IZb HTTP/1.1" 200 None
2017-06-04 14:21:51,374 - requests.packages.urllib3.connectionpool - DEBUG - https://aip.baidubce.com:443 "POST /rpc/2.0/nlp/v2/comment_tag?aipSdk=python&aipVersion=1_4_0&access_token=24.2f65885acf583173d679ec84d37a04a5.2592000.1499149310.282335-9723636 HTTP/1.1" 200 79    

---
# access_token
访问百度api
access_token=24.27d95f96bd8c8c6ed15208b7ba287447.2592000.1499160083.282335-9723636

access_token=24.97285d47c87d8a735b6e491e8290c6d5.2592000.1499161262.282335-9723636

24.d648b7a82d965179ff55a84a5ca10ce2.2592000.1499176480.282335-9723636

https://login.bce.baidu.com/