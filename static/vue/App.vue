<template>
    <div id="template-weather">
      <div class="site-blocks-cover" style="background-image: url(static/images/hero_bg_1.jpg);" data-aos="fade" data-stellar-background-ratio="0.5">
        <div class="container">
          <div class="row row-custom align-items-center">
            <div class="col-md-10">
              <h1 class="mb-2 text-gray-69 w-75"><span class="font-weight-bold">旅行へ向けの服装</span></h1>
              <div class="job-search">
                <div class="tab-content bg-white p-4 rounded" id="pills-tabContent">
                  <div class="tab-pane fade show active" id="pills-job" role="tabpanel" aria-labelledby="pills-job-tab">
                    <!-- <form action="#" method="post"> -->
                      <div class="row">
                        <div class="col-md-6 col-lg-3 mb-3 mb-lg-0">
                          <div class="select-wrap">
                            <span class="icon-keyboard_arrow_down arrow-down"></span>
                            <select name="city" id="" class="form-control">
                              <option 
                                :value="key" 
                                @click="selectCity(c)" 
                                :selected="c.id === default_id"
                                v-for="(c, key) in cities">{{c.city_name}}</option>
                            </select>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-3 mb-3 mb-lg-0" id="start_date">
                          <div class="input-group date">
                            <input type="text" class="form-control" id="s_date" placeholder="出発日">
                            <span class="input-group-addon"></span>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-3 mb-3 mb-lg-0" id="end_date">
                          <div class="input-group date">
                            <input type="text" class="form-control" id="e_date" placeholder="帰国日">
                            <span class="input-group-addon"></span>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-3 mb-3 mb-lg-0">
                          <button id="search_button" id="search_btn" class="btn btn-primary btn-block" @click="searchRecommend">検索</button>
                        </div>
                      </div>
                    <!-- </form> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div class="site-section bg-light py-4" id="result_section">
        <div class="container">
          <div class="row justify-content-start text-left mb-5">
            <div class="col-md-9" data-aos="fade">
              <h2 class="font-weight-bold">おすすめ</h2>
            </div>
          </div>
  
          <div class="bg-white p-2 my-3 shadow row" v-for="re in selected_recommend">
            <div class="col-2">
              <div class="card h-100 py-5">
                <div class="card-body text-center p-0">
                  <p class="card-title font-weight-bold date">２／１</p>
                  <p class="card-title font-weight-bold date">（月）</p>
                  <div class="d-none d-md-block">
                    <div class="row p-0 w-75 m-auto">
                      <div class="col-md-6 text-primary p-0 border-right border-secondary">15 &ordm; C</div>
                      <div class="col-md-6 text-danger p-0">25 &ordm; C</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="result-element col-10 list-group list-group-horizontal-md flex-fill">
                <div class="col-md-4 list-group-item">
                  <div class="row">
                    <div class="col-6 col-md-12 border-bottom text-center weather-info pb-2">
                      <div class="row">
                        <div class="col-md-2 p-0 font-weight-bold">
                          <p class="time bg-morning rounded text-white p-1">朝</p>
                          <h5>晴れ</h5>
                        </div>
                        <div class="col-md-7">
                          <img src="static/images/sun1.jpeg" class="img-fluid" alt="">
                        </div>
                        <div class="col-md-3 p-0 d-flex flex-column">
                          <span class="text-primary">15 &ordm; C</span>
                          <span class="text-danger">25 &ordm; C</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-6 col-md-12 py-3">
                      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, totam?
                    </div>
                  </div>
                </div>
                <div class="col-md-4 list-group-item">
                  <div class="row">
                    <div class="col-6 col-md-12 border-bottom text-center weather-info pb-2">
                      <div class="row">
                        <div class="col-md-2 p-0 font-weight-bold">
                          <p class="time bg-afternoon rounded text-white p-1">昼</p>
                          <h5>晴れ</h5>
                        </div>
                        <div class="col-md-7">
                          <img src="static/images/sun1.jpeg" class="img-fluid" alt="">
                        </div>
                        <div class="col-md-3 p-0 d-flex flex-column">
                          <span class="text-primary">15 &ordm; C</span>
                          <span class="text-danger">25 &ordm; C</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-6 col-md-12 py-3">
                      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, totam?
                    </div>
                  </div>
                </div>
                <div class="col-md-4 list-group-item">
                  <div class="row">
                    <div class="col-6 col-md-12 border-bottom text-center weather-info pb-2">
                      <div class="row">
                        <div class="col-md-2 p-0 font-weight-bold">
                          <p class="time bg-night rounded text-white p-1">夜</p>
                          <h5>晴れ</h5>
                        </div>
                        <div class="col-md-7">
                          <img src="static/images/sun1.jpeg" class="img-fluid" alt="">
                        </div>
                        <div class="col-md-3 p-0 d-flex flex-column">
                          <span class="text-primary">15 &ordm; C</span>
                          <span class="text-danger">25 &ordm; C</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-6 col-md-12 py-3">
                      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, totam?
                    </div>
                  </div>
                </div>
            </div>
          </div>
          
        </div>
      </div>
  
    </div>
</template>
<script type="module">
    module.exports = {
        data: function() {
            return {
                cities: [],
                host: 'http://localhost:5000/',
                recommend: {},
                selected_city: "",
                s_date: "",
                e_date: "",
                default_id: 0,
                selected_recommend: [],
                morning: "06:00",
                afternoon: "12:00",
                night: "21:00"
            }
        },
        mounted() {
            this.getListCities()
        },
        methods: {
            httpGetAsync(theUrl, callback, city_code) {
                let xmlHttp = new XMLHttpRequest();
                xmlHttp.onreadystatechange = function() { 
                    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                        callback(xmlHttp.responseText, city_code);
                }
                xmlHttp.open("GET", theUrl, true); // true for asynchronous 
                xmlHttp.send(null);
            },

            getListCities() {
                let url = this.host + 'list'
                this.httpGetAsync(url, this.showCities)
            },

            showCities(data) {
                this.cities = JSON.parse(data)

                if(this.cities !== undefined) {
                    Object.keys(this.cities).forEach((key) => {
                        if(this.cities[key].city_code !== undefined) {
                            console.log(key, this.cities[key], this.cities[key].city_code);
                            this.getWeather(this.cities[key].city_code)
                            if(this.cities[key].id === 0) {
                                this.selected_city = this.cities[key]
                            }                            
                        }
                    });
                }
            },

            getWeather(city_code) {
                let url = this.host + 'recommend' + '?city_code=' + city_code
                this.httpGetAsync(url, this.showData, city_code)
            },

            showData(data, city_code) {
                let d = JSON.parse(data)
                this.recommend[city_code] = d
                if(city_code == 'hanoi') {
                    this.selected_recommend = this.groupDate(this.recommend[city_code])
                }
            },

            selectCity(c) {
                this.selected_city = c
            },

            compareDate(str_start, str_end, str_date) {
                let start = new Date(str_start)
                let start_date = start.getDate()
                let start_month = start.getMonth()
                let end = new Date(str_end)
                let end_date = end.getDate()
                let end_month = end.getMonth()
                let d = new Date(str_date)
                let d_date = d.getDate()
                let d_month = d.getMonth()
                if(d_month >= start_month && d_month <= end_month) {
                    if(d_date >= start_date && d_date <= end_date) {
                        return true
                    }
                }
                return false
            },

            isEqualDate(str_start, str_end) {
                let start = new Date(str_start)
                let start_date = start.getDate()
                let start_month = start.getMonth()
                let end = new Date(str_end)
                let end_date = end.getDate()
                let end_month = end.getMonth()
                if(start_date == end_date && start_month == end_month) {
                    return true
                }
                return false
            },

            groupDate(recommend) {
                let t = []
                let re = []
                let before_val = ""
                recommend.forEach(r => {
                    if(before_val === "" || this.isEqualDate(before_val, r.dt_txt)) {
                        t.push(r)
                    }
                    else {
                        re.push(t)
                        t = []
                        t.push (r)
                    }
                    before_val = r.dt_txt
                })
                re.push(t)
                return re
            },

            getDate(str_date) {
                return (new Date(str_date)).getDate()
            },

            getMonth(str_date) {
                return (new Date(str_date)).getMonth()
            },

            searchRecommend() {
                let selected_city = this.selected_city
                s_date = document.getElementById('s_date').value
                e_date = document.getElementById('e_date').value
                console.log(selected_city, (new Date(s_date)).getDate(), (new Date(e_date)).getDate())
                if (selected_city.city_code in this.recommend) {
                    let tmp = this.recommend[selected_city.city_code]
                    console.log('tmp', tmp, (new Date("2020-02-19 12:00:00")).getDate())
                    let r_filter = tmp.filter((r) => this.compareDate(s_date, e_date, r.dt_txt))
                    
                    this.selected_recommend = this.groupDate(r_filter)
                    console.log(this.selected_recommend);
                }
            },

            // getTime(date) {
            //     d = new Date(date)
            //     let hour = d.getHours().toString()
            //     let time = ""
            //     console.log(getTime)
            //     if(hour === this.morning) {
            //         time = "朝"
            //     }
            //     if(hour === this.afternoon) {
            //         time = "昼"
            //     }
            //     if(hour === this.night) {
            //         time = "夜"
            //     }
            //     return time

            // }

        }
    }
</script>