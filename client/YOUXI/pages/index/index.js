Page({
  data: {
    array: ['国内', '国际', '财经', '娱乐', '军事', '体育', '其他'],
    nav: 0,
    news: [],
    top: {}
  },

  onLoad() {
    this.getList(0);
  },

  onPullDownRefresh() {
    const type = this.data.nav;
    this.getList(type, () => {
      wx.stopPullDownRefresh();
    })
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
    let type = v;
    switch (type) {
      case '0':
        type = 'gn';
        break;
      case '1':
        type = 'gj';
        break;
      case '2':
        type = 'cj';
        break;
      case '3':
        type = 'yl';
        break;
      case '4':
        type = 'js';
        break;
      case '5':
        type = 'ty';
        break;
      case '6':
        type = 'other';
        break;
      default:
        type = 'gn';
    }
    wx.showLoading({
      title: "加载中"
    })
    wx.request({
      url: `https://test-miniprogram.com/api/news/list?type=${type}`,
      method: 'GET',
      success: res => {
        const result = res.data.result.map(v => ({
          id: v.id,
          firstImage: v.firstImage.length > 0 ? v.firstImage : '../../images/news.jpg',
          title: v.title,
          source: v.source,
          date: v.date.slice(0, 10)
        }));
        console.log(result);
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
