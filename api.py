

def server_api():
    servers = {
  'start-luckydb-uat':      [ 'https://oq78pwdh4d.execute-api.us-east-1.amazonaws.com/default/StartLuckyDbUat','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','LuckyDB server-UAT'],
  'stop-luckydb-uat':       [ 'https://li4a4lt165.execute-api.us-east-1.amazonaws.com/default/StopLuckyDbUat', 'https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','LuckyDB server-UAT'],
  'start-adtech-qa-matomo': [ 'https://mko1fjxnwk.execute-api.us-east-1.amazonaws.com/default/StartAdtechQa', 'https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','Adtech-QA Matomo'],
  'stop-adtech-qa-matomo':  [ 'https://eka9e96n6g.execute-api.us-east-1.amazonaws.com/default/StopAdtechQa',  'https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','Adtech-QA Matomo'],
  'start-mhmysql-qa':       [ 'https://vdrgmucdhi.execute-api.us-east-1.amazonaws.com/default/StartMessageHubMysqlQa','https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub QA-Mysql' ],
  'stop-mhmysql-qa':        [ 'https://p0y15dic72.execute-api.us-east-1.amazonaws.com/default/StopMessageHubMysqlQa', 'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub QA-Mysql'],
  'start-mymed-qa':         [ 'https://o6yik68b5k.execute-api.us-east-1.amazonaws.com/default/StartMymedQa','https://chat.googleapis.com/v1/spaces/AAAAbbMj5yE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=AQ4ID1lvuzmJECYn9fDOHeePgvyrLAUmltIecSS13Hc%3D','Mymed QA'],
  'stop-mymed-qa':          [ 'https://5pgbsa4es6.execute-api.us-east-1.amazonaws.com/default/StopMymedQa', 'https://chat.googleapis.com/v1/spaces/AAAAbbMj5yE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=AQ4ID1lvuzmJECYn9fDOHeePgvyrLAUmltIecSS13Hc%3D','Mymed QA'],
  'start-starfriends-uat':  [ 'https://lcxa8ld10d.execute-api.us-east-1.amazonaws.com/default/StartStarFriendsUat','https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','StarFriends (UAT)'],
  'stop-starfriends-uat':   [  'https://hxm2jp2phe.execute-api.us-east-1.amazonaws.com/default/StopStarFriendsUat', 'https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','StarFriends (UAT)'],
  'start-lucky-dev':        [ 'https://qsofl9kqb2.execute-api.us-east-1.amazonaws.com/default/StartLuckyDev','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1 DEV Server - V1'],
  'stop-lucky-dev':         [  'https://qjn555djb7.execute-api.us-east-1.amazonaws.com/default/StopLuckyDev','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1 DEV Server - V1'],
  'start-adtech-qa-test':   [ 'https://0espsdwvg9.execute-api.us-east-1.amazonaws.com/default/StartAdtechQaTestApp','https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','AdTech-QA Test APP'],
  'stop-adtech-qa-test':    [ 'https://l4kycm60vi.execute-api.us-east-1.amazonaws.com/default/StopAdtechQaTestApp', 'https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','AdTech-QA Test APP'],
  'start-mh-dev':           [  'https://4v1p0tuorl.execute-api.us-east-1.amazonaws.com/default/StartMessageHubDev', 'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub-dev'],
  'stop-mh-dev':            [  'https://2w089spn1c.execute-api.us-east-1.amazonaws.com/default/StopMessageHubDev',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub-dev'],
  'start-mh-qa':            [   'https://stgpzfale4.execute-api.us-east-1.amazonaws.com/default/StartMessageHubQa', 'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub - QA'],
  'stop-mh-qa':             [  'https://stgpzfale4.execute-api.us-east-1.amazonaws.com/default/StartMessageHubQa',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub - QA'],
  'start-lucky-qa-bo':      ['https://bgbqh2rc44.execute-api.us-east-1.amazonaws.com/default/StartLuckyQaBo','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1 Dev/QA/Staging/Uat Server - BO'],
   'stop-lucky-qa-bo':       ['https://93lcev3z2g.execute-api.us-east-1.amazonaws.com/default/StopLuckyQaBo','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1 Dev/QA/Staging/Uat Server - BO'],
  'start-mhmongo-qa':       [  'https://z01abhe6mi.execute-api.us-east-1.amazonaws.com/default/StartMhMongoQa',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub - QA - mongodb'],
  'stop-mhmongo-qa':        [  'https://nwjdltk14d.execute-api.us-east-1.amazonaws.com/default/StopMhMongoQa',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub - QA - mongodb'],
  'start-pandacampus-qa':   [  'https://0i71nj7w6j.execute-api.us-east-1.amazonaws.com/default/StartPandaCampusQa', 'https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','PandaCampus (dev , qa , staging , uat)'],
  'stop-pandacampus-qa':    [  'https://87rgxjok19.execute-api.us-east-1.amazonaws.com/default/StopPandaCampusQa', 'https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','PandaCampus (dev , qa , staging , uat)'],
  'start-ibid-qa':          [  'https://a9ncdydesg.execute-api.us-east-1.amazonaws.com/default/StartIbidQa','https://chat.googleapis.com/v1/spaces/AAAAWzn8T08/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=vuMvk3Er_1LXPiSQNQ_IWFghXyn8Y6mOqNy6GnkJjtY%3D','IBid (dev , qa, staging)'],
  'stop-ibid-qa':           [ 'https://f2ek3wkc3f.execute-api.us-east-1.amazonaws.com/default/StopIbidQa', 'https://chat.googleapis.com/v1/spaces/AAAAWzn8T08/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=vuMvk3Er_1LXPiSQNQ_IWFghXyn8Y6mOqNy6GnkJjtY%3D','IBid (dev , qa, staging)'],
  'start-mh-uat':           [ 'https://5scqeecxnh.execute-api.us-east-1.amazonaws.com/default/StartMhUat',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub-UAT'],
  'stop-mh-uat':            [ 'https://is0lot6lla.execute-api.us-east-1.amazonaws.com/default/StopMhUat',  'https://chat.googleapis.com/v1/spaces/AAAAMOQp4HQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=d_hI2p9EyQVXpvxW80do8dP93TAHacx-FsdebPnO_P0%3D','Messagehub-UAT'],
  'start-lucky-uat':        [ 'https://a700x10r8g.execute-api.us-east-1.amazonaws.com/default/StartLuckyUat','https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1-UAT'],
  'stop-lucky-uat':         [  'https://54nipv5nbe.execute-api.us-east-1.amazonaws.com/default/StopLuckyUat',  'https://chat.googleapis.com/v1/spaces/AAAAsFwk3hY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jhpeIFfwdzWZMH-W2cHPwGV7GmfpLx6Xz00Xwd4J3dQ%3D','Lucky1-UAT'],
  'start-adtechcore-qa':    [ 'https://56ixk8qqwc.execute-api.us-east-1.amazonaws.com/default/StartAdtechCoreQa', 'https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','AdTech-QA Core+Dependencies'],
  'stop-adtechcore-qa':     [ 'https://82l3lfe4o9.execute-api.us-east-1.amazonaws.com/default/StopAdtechCoreQa',  'https://chat.googleapis.com/v1/spaces/AAAAJyv11No/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5duznv6qp_IFqyVYTDt7fXO8Lsj8onWg4OEQX9XKSjE%3D','AdTech-QA Core+Dependencies'],
  'start-starfriends-qa':   [  'https://3srmz8vq34.execute-api.us-east-1.amazonaws.com/default/StartStarFriendsPopcornQa' ,'https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','starfriends-qa'],
  'stop-starfriends-qa':    [ 'https://pd97jn3ob0.execute-api.us-east-1.amazonaws.com/default/StopStarFriendsPopcornQa' ,'https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','StarFriends/Popcorn (dev , qa, staging)' ],
  'start-starfriends-newdev':['https://lek3jtvn3i.execute-api.us-east-1.amazonaws.com/default/StartStarfriendsNewDev','https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','StarFriendsNewDev'],
  'stop-starfriends-newdev':['https://8ztcm8jimd.execute-api.us-east-1.amazonaws.com/default/StopStarfriendsNewDev','https://chat.googleapis.com/v1/spaces/AAAATqj1csA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DKPw1Jalm8GM8AHUSua9sSYETn1Ldx7ykjD2KhV69N0%3D','StarFriendsNewDev']
}

    return servers