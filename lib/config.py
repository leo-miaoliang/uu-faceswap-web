class Config:
    SECRET_KEY = ''
    SECRET_PWD = ''

class DEVConfig(Config):
    WORK_DIR = "/home/crh/uu-project/AI/uu-faceswap/dir"
    HOST = 'rm-bp15do63ws7rs648qvo.mysql.rds.aliyuncs.com'
    PORT = 3306
    USER = 'user_ulive'
    PASSWORD = 'Uuabc2019&g.1'
    DB = 'ulive'

class PRDConfig(Config):
    WORK_DIR = "/home/crh/uu-project/AI/uu-faceswap/dir"
    HOST = 'rm-bp15do63ws7rs648qvo.mysql.rds.aliyuncs.com'
    PORT = 3306
    USER = 'user_ulive'
    PASSWORD = 'Uuabc2019&g.1'
    DB = 'ulive'

config = {
    'dev': DEVConfig,
    'prd': PRDConfig,
    'production': PRDConfig,
    'default': DEVConfig
}