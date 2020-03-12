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
                            <select name="city" id="" class="form-control" @change="selectCity">
                              <option 
                                :value="key" 
                                v-on:click="() => {alert(1)}"
                                :selected="c.id === default_id"
                                v-for="(c, key) in cities">{{c.city_name}}</option>
                            </select>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-3 mb-3 mb-lg-0" id="start_date">
                          <div class="input-group date" >
                            <input type="text" class="form-control" id="s_date" ref="st_date" placeholder="出発日">
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
                        <span class="text-secondary text-sm pt-2 pl-3">＊　本日より５日以内の日付のみ選択できます</span>
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
          <div class="b-bottom">
            <h2 class="font-weight-bold" v-if="selected_city.city_code == 'hanoi'">ハノイの天気</h2>
            <h2 class="font-weight-bold" v-else>ダナンの天気</h2>
            <h4 v-html="weather_description" class="my-4"></h4>
          </div>
          <div class="row justify-content-start text-left mb-3 mt-3">
            <div class="col-md-9" data-aos="fade">
              <h2 class="font-weight-bold">滞在中におすすめの服装</h2>
            </div>
          </div>
          <template v-if="mode === 'sixteen'">
            <div class="bg-white p-2 my-3 shadow row" v-for="re in selected_recommend">
              <!-- <div class="col-md-2 "> -->
                <!-- <div class="card h-100 py-5">
                  <div class="card-body text-center p-0">
                    <p class="card-title font-weight-bold date">{{getDateInfo(re).month}} / {{getDateInfo(re).date}}</p>
                    <p class="card-title font-weight-bold date">（{{getDateInfo(re).day}}）</p>
                    <div class="">
                      <div class="row p-0 w-75 m-auto">
                        <div class="col-md-6 text-primary p-0 border-right border-secondary">{{toIntNum(re.temp_min)}} &ordm; C</div>
                        <div class="col-md-6 text-danger p-0">{{toIntNum(re.temp_max)}} &ordm; C</div>
                      </div>
                    </div>
                  </div>
                </div> -->
                <div class="col-md-2 py-3 text-center border d-flex justify-content-center">
                  <div class="row align-self-center">
                    <div class="col-6 col-md-12 py-1">
                      <div class="text-center">
                        <span class="font-weight-bold date">{{getDateInfo(re).month}} / {{getDateInfo(re).date}}</span>
                        <span class="font-weight-bold date">（{{getDateInfo(re).day}}）</span>
                      </div>
                      <div class="d-flex justify-content-center">
                        <span class="text-primary px-2 border-right border-secondary">{{toIntNum(re.temp_min)}} &ordm; C</span>
                        <span class="text-danger px-2">{{toIntNum(re.temp_max)}} &ordm; C</span>
                      </div>
                    </div>
                    <div class="col-4 col-md-12 py-1">
                      <div class="w-md-75 mx-auto">
                        <img :src="re.images" alt="static/images/logo.jpeg" class="img-fluid" alt="">
                      </div>
                    </div>
                    <div class="col-2 col-md-12 py-1">
                      <h5>{{re.type}}</h5>
                    </div>
                  </div>
                </div>
              <!-- </div> -->
              <div class="result-element col-md-10 p-0 list-group list-group-horizontal-md flex-fill">
                <div class="col-md-4 list-group-item" v-for="(data, index) in re.recommend">
                  <div class="row">
                    <div class="col-12 text-center weather-info border-bottom">
                      <div class="d-flex justify-content-between font-weight-bold">
                        <div class="p-0">
                          <p class="time rounded text-white p-1 morning_color" v-if="index == 0">朝</p>
                          <p class="time rounded text-white p-1 afternoon_color" v-if="index == 1">昼</p>
                          <p class="time rounded text-white p-1 night_color" v-if="index == 2">夜</p>
                        </div>
                        <div class="p-0">
                          <span class="mr-2">体感温度</span>
                          <span class="text-danger" v-if="index == 0">{{toIntNum(re.temp_morn)}} &ordm; C</span>
                          <span class="text-danger" v-if="index == 1">{{toIntNum(re.temp_day)}} &ordm; C</span>
                          <span class="text-danger" v-if="index == 2">{{toIntNum(re.temp_night)}} &ordm; C</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-12 py-3">
                      <span v-html="data"></span>
                      <div class="fashion-list">
                        <button type="button" class="btn btn-sm btn-warning">テーシャツ</button>
                        <button type="button" class="btn btn-sm btn-info">靴</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
          <template v-else>
            <div class="bg-white p-2 my-3 shadow row" v-for="re in selected_recommend">
              <div class="col-md-2">
                <div class="card h-100 d-none d-md-block py-5">
                  <div class="card-body text-center p-0">
                    <p class="card-title font-weight-bold date">{{getDateInfo(re).month}} / {{getDateInfo(re).date}}</p>
                    <p class="card-title font-weight-bold date">（{{getDateInfo(re).day}}）</p>
                    <div class="d-none d-md-block">
                      <div class="row p-0 w-75 m-auto">
                        <div class="col-md-6 text-primary p-0 border-right border-secondary">{{toIntNum(getDateInfo(re).min)}} &ordm; C</div>
                        <div class="col-md-6 text-danger p-0">{{toIntNum(getDateInfo(re).max)}} &ordm; C</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="h-100 d-block d-md-none">
                  <div class="card-body text-center p-0">
                    <span class="card-title font-weight-bold date">{{getDateInfo(re).month}} / {{getDateInfo(re).date}}</span>
                    <span class="card-title font-weight-bold date">（{{getDateInfo(re).day}}）</span>
                  </div>
                </div>
              </div>
              <div class="result-element col-md-10 list-group list-group-horizontal-md flex-fill">
                <div class="col-md-4 list-group-item" v-for="(data, index) in re">
                  <div class="row">
                    <div class="col-12 py-3">
                      <span v-html="data.recommend"></span>
                      <div class="fashion-list">
                        <button type="button" class="btn btn-sm btn-warning">テーシャツ</button>
                        <button type="button" class="btn btn-sm btn-info">靴</button>
                      </div>
                    </div>
                    <div class="col-12 text-center weather-info pt-3 border-top">
                      <div class="row">
                        <div class="col-2 p-0 font-weight-bold">
                          <p class="time rounded text-white p-1 morning_color" v-if="index == 0">朝</p>
                          <p class="time rounded text-white p-1 afternoon_color" v-if="index == 1">昼</p>
                          <p class="time rounded text-white p-1 night_color" v-if="index == 2">夜</p>
                          <h5>{{data.type}}</h5>
                        </div>
                        <div class="col-5">
                          <img :src="data.images" alt="static/images/logo.jpeg" class="img-fluid" alt="">
                        </div>
                        <div class="col-5 p-0 d-flex flex-column">
                          <span class=""><体感温度></span>
                          <span class="text-danger">{{toIntNum(data.feels_like)}} &ordm; C</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
          
          
        </div>
      </div>
      <div class="site-secsion bg-white py-5" id="instagram_recommends">
        <div class="container">
          <div class="row justify-content-start text-left mb-5">
            <div class="col-md-9" data-aos="fade">
              <h2 class="font-weight-bold">レコメンドスナップ</h2>
            </div>
          </div>
          <div class="row" id="instagram_div">
            <div class="col-md-4 shadow p-3">
              <span v-html="selected_instagram.image_1"> </span>
            </div>
            <div class="col-md-4 shadow p-3">
              <span v-html="selected_instagram.image_2"> </span>
            </div>
            <div class="col-md-4 shadow p-3">
              <span v-html="selected_instagram.image_3"> </span>
            </div>
            <div id='add-script'>
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
                mode: 'sixteen', // if want change mode to five days, set "mode: 'five'"
                cities: [],
                host: 'http://localhost:5000/',
                recommend: {},
                selected_city: "",
                s_d: "",
                e_d: "",
                default_id: 0,
                selected_recommend: [],
                morning: "06:00",
                afternoon: "12:00",
                night: "21:00",
                selected_instagram: {},
                weatherConditions: [],
                list_instas: [],
                weather_description: ""
            }
        },
        mounted() {
            this.getListCities()
            this.getWeatherConditions()
            this.getInstaJson()
            let d = new Date();
            let n = d.getMonth();
            if(this.mode == 'five') {
              $(document).ready(function () {
              var start_date = new Date();
              var end_date = new Date();
              end_date.setDate(end_date.getDate() + 4);
              $('#start_date .date, #end_date .date').datepicker({
                  startDate: start_date,
                  endDate: end_date,
                  language: "ja",
                  autoclose: true,
                  todayHighlight: true
              });
            })
            }
            else {
              $(document).ready(function () {
              var start_date = new Date();
              var end_date = new Date();
              end_date.setDate(end_date.getDate() + 15);
              $('#start_date .date, #end_date .date').datepicker({
                  startDate: start_date,
                  endDate: end_date,
                  language: "ja",
                  autoclose: true,
                  todayHighlight: true
              });
            })
            }
            
            
        },
      
        computed: {
          'start_date_value': function() {
            if(this.$refs.st_date) {
              return this.$refs.st_date.value
            }
            else return 1
          }
        },
        watch: {
          'start_date_value': function() {
            $('#end_date .date').datepicker({
                  startDate: this.s_date,
                  endDate: end_date,
                  language: "ja",
                  autoclose: true,
                  todayHighlight: true
              });
          },
          'selected_city': function() {
            if(this.list_instas.length) {
              let d = new Date();
              let n = d.getMonth();
              this.selected_instagram = this.list_instas[this.selected_city.city_code][n]
            }
          }
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

            getInstaJson() {
              let url = this.host + 'insta'
              this.httpGetAsync(url, this.handleInsta)
            },

            handleInsta(data) {
              data = JSON.parse(data)
              this.list_instas = data
              console.log(data)
              let d = new Date();
              let n = d.getMonth();
              this.selected_instagram = data[this.selected_city.city_code][n]
              let insta = document.createElement('script');  
              insta.setAttribute('src',"https://www.instagram.com/static/bundles/es6/EmbedSDK.js/bf4a12bd69f3.js");
              document.getElementById('add-script').append(insta)
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
                            this.getWeather(this.cities[key].city_code)
                            if(this.cities[key].id === 0) {
                                this.selected_city = this.cities[key]
                                let d = new Date();
                                let n = d.getMonth();
                                this.weather_description = this.selected_city.weather_description[n]
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
                console.log("datas: ", d, "city_code: ", city_code, d.length)
                
                this.recommend[city_code] = d
                if(city_code == 'hanoi') {
                    if(this.mode == 'five') {
                      this.selected_recommend = this.groupDate(this.recommend[city_code])
                    } else {
                      this.selected_recommend = this.recommend[city_code]
                    }
                }
            },

            selectCity(c) {
                this.selected_city = this.cities[c.target.value]
                let d = new Date();
                let n = d.getMonth();
                this.selected_instagram = this.list_instas[this.selected_city.city_code][n]
                this.weather_description = this.selected_city.weather_description[n]
            },

            getWeatherConditions() {
              let url = this.host + 'weather-conditions'
              this.httpGetAsync(url, this.showWeatherConditions)
            },

            showWeatherConditions(data) {
              this.weatherConditions = JSON.parse(data)
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
                return (new Date(str_date)).getMonth() + 1
            },

            getDay(str_date) {
              let day = (new Date(str_date)).getDay()
              let str_day = ''
              switch(day) {
                case 0: str_day = '日'; break;
                case 1: str_day = '月'; break;
                case 2: str_day = '火'; break;
                case 3: str_day = '水'; break;
                case 4: str_day = '木'; break;
                case 5: str_day = '金'; break;
                case 6: str_day = '土'; break;
              }
              return str_day
            },

            validation() {
              s_date = document.getElementById('s_date').value
              e_date = document.getElementById('e_date').value
              if(s_date == "") {
                toastr.warning("Start Date False")
                return false
              }
              if(e_date == "") {
                toastr.warning("End Date False")
                return false
              }
              if(e_date < s_date) {
                toastr.warning("End Date less than Start Date")
                return false
              }
              return true
            },

            searchRecommend() {
                if(this.validation()) {
                  $([document.documentElement, document.body]).animate({
                          scrollTop: $("#result_section").offset().top
                      }, 1000);
                  let selected_city = this.selected_city
                  s_date = document.getElementById('s_date').value
                  e_date = document.getElementById('e_date').value
                  // console.log(selected_city, (new Date(s_date)).getDate(), (new Date(e_date)).getDate())
                  if (selected_city.city_code in this.recommend) {
                      let tmp = this.recommend[selected_city.city_code]
                      // console.log('tmp', tmp, (new Date("2020-02-19 12:00:00")).getDate())
                      let r_filter = tmp.filter((r) => this.compareDate(s_date, e_date, r.dt_txt))
                      if(this.mode == 'five') {
                        this.selected_recommend = this.groupDate(r_filter)
                      }
                      this.selected_recommend = r_filter
                      
                      // console.log(this.selected_recommend);
                  }
                }
            },

            getMin(data) {
              let min = 100
              data.forEach(d => {
                if(min >= d.temp_min) {
                  min = d.temp_min
                }
              })
              return min
            },

            getMax(data) {
              let max = -100
              data.forEach(d => {
                if(max <= d.temp_max) {
                  max = d.temp_max
                }
              })
              return max
            },

            getDateInfo(data) {
              let info = {}
              if(this.mode == 'five') {
                  info['date'] = this.getDate(data[0].dt_txt)
                  info['month'] = this.getMonth(data[0].dt_txt) 
                  info['day'] = this.getDay(data[0].dt_txt)
                }
                else {
                  info['date'] = this.getDate(data.dt_txt)
                  info['month'] = this.getMonth(data.dt_txt) 
                  info['day'] = this.getDay(data.dt_txt)
                }
              return info
              
            },

            toIntNum(f_num) {
              return Math.round(f_num)
            }

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


<style>
  .morning_color {
    background: #f62e36;
  }
  .afternoon_color {
    background: #ff9500;
  }
  .night_color {
    background: #009bbf;
  }
  .display-none {
    display: none !important;
  }
  .b-bottom {
    border-bottom: 1px solid #dad8d8;
  }
  
</style>