from qiniu import Auth


def get_qiniu_token(file_key):
    access_key = 'jmqcTEbGcBacoAYUSzUY3gDXSLUVX6_YHfIjtF5F'
    secret_key = 'rsBJgoKKtzKi2H7DIyh-p2gWMqfEP6j_EgKlZIEe'
    # 构建鉴权对象
    q = Auth(access_key=access_key, secret_key=secret_key)
    # 要上传的空间
    bucket_name = 'qaclass'

    # 上传后保存的文件名
    key = file_key
    # 生成token，可以指定过期时间
    token = q.upload_token(bucket_name, key, 3600)
    return token
