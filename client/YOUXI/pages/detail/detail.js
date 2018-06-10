// pages/detail/detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    article: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getDetail(options.id);
  },
  getDetail(id) {
    wx.request({
      url: `https://test-miniprogram.com/api/news/detail?id=${id}`,
      method: 'GET',
      success: res => {
        this.setData({
          article: res.data.result
        })
      }
    })
  },

  goback() {
    wx.navigateBack({});
  }
})