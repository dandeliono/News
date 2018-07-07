Page({
  data: {
    array: ['热点', '单机', '网游', '影视', '动漫', '周边'],
    nav: 0,
    news: [],
    top: {},
    count:10
  },

  onLoad() {
    this.getList(5);
  },
  onPullDownRefresh() {
    const type = this.data.nav;
    var count = this.data.count + 10
    this.setData({
      count: count,
    })
    this.getList(type, () => {
      wx.stopPullDownRefresh();
    })
  },
  
  onReachBottom: function () {
    console.log(this.data)
    setTimeout(() => {
      var count = this.data.count +10
      this.setData({
        count: count,
      })
    }, 100)
  },
  setNav(e) {
    const index = e.currentTarget.id;
    this.setData({
      nav: index,
    })
    this.getList(index);
  },

  getList(v, callback) {
    var that = this;
    let type = this.data.array[v];
    if(type === '热点'){
      type = '周边'
    }
    
    
    wx.showLoading({
      title: "加载中"
      
    })

    wx.request({
      url: `http://127.0.0.1:9600/newsTitle?type=${type}`,
      method: 'GET',
      success: res => {
        const result = res.data.result.map(v => ({
          id: v.jumpUrl,
          firstImage: v.imgSrc.length > 0 ? v.imgSrc : '../../images/news.jpg',
          title: v.title,
          source: v.source,
          date: v.date
        }));

        const top = result[0];
        result.shift();
        that.setData({
          news: result,
          top: top,
        })
      },
      complete: () => {
        wx.hideLoading();
        callback && callback();
      }
    })
  },

  toDetail(e) {
    const id = e.currentTarget.id;
    wx.navigateTo({
      url: `../detail/detail?id=${id}`,
    })
  }
})
