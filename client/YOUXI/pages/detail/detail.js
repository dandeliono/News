// pages/detail/detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    article: '',
    comments:''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.getDetail(options.id);
  },

  getDetail(id) {
    console.log(id)
    var app = getApp();

    var openid = app.globalData.openid
    wx.request({
      url: `http://127.0.0.1:9600/newsDetail?hash=${id}&openid=${openid}`,
      method: 'GET',
      success: res => {
        this.setData({
          article: res.data.result
        })
        console.log(res.data)
      }
    })
    console.log(this.data.article)

  },

  goback() {
    wx.navigateBack({});
  },
  bindReply: function(e) {
    this.setData({
      releaseFocus: true
    })
  },
  replyfinish() {
    var comm = this.data.comments + this.data.comment + '\n'
    this.setData({
        releaseFocus: false,
        comments:comm
      })
    console.log(this.data.comments)
    var app = getApp();
    var openid = app.globalData.openid
      wx.request({
        url: "http://127.0.0.1:9600/comment",
        method: "POST",
        data: {
          openid: openid,
          comment: this.data.comment,
          title: this.data.article.title
        },
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        success: function(res) {
          console.log(res.data);
          wx.showToast({
            title: '评论成功！',
            icon: 'success',
            duration: 2000
          })
        }

      })
  },
  reply: function(e) {
    this.setData({
      comment: e.detail.value
    });
  }
})