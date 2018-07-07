//app.js
App({
  globalData: {
    a: 'https://test-miniprogram.com',
    openid: ''
  },
  onLaunch: function () {
    wx.login({
      success: function (res) {
        if (res.code) {
          //发起网络请求
          wx.request({
            url: 'http://127.0.0.1:9600/onLogin',
            data: {
              code: res.code
            },
            success: function (res) {
              var app = getApp();
             
              app.globalData.openid = res.data
              
            }
          })
          console.log(res.code);
        } else {
          console.log('登录失败！' + res.errMsg)
        }
      }
    });

    console.log(this.globalData.openid)
  }
})