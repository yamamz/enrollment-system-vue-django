.<template>
  <div id="app" style="padding: 20px 20px;">
    <div class="semipolar-spinner" v-show="isLoading">
      <div class="ring"></div>
      <div class="ring"></div>
      <div class="ring"></div>
      <div class="ring"></div>
      <div class="ring"></div>
      <br />
      <br />
      <br />
      <p>Feching</p>
    </div>
    <el-card>
      <h6>Search Parameters</h6>
      <div>
        <el-row :gutter="5">
          <el-col :md="8">
            <el-select
              filterable
              style="width: 100%;"
              size="small"
              v-model="course"
              placeholder="select course"
            >
              <el-option value="">select course</el-option>
              <el-option
                v-for="(item, index) in courses"
                :key="index"
                :label="item.code"
                :value="item.code"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="major"
              placeholder="select major"
            >
              <el-option value="">select major</el-option>
              <el-option
                v-for="(item, index) in majors"
                :key="index"
                :label="item.name"
                :value="item.name"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="sem"
              placeholder="select semister"
            >
              <el-option value="">select semister</el-option>
              <el-option
                v-for="(item, index) in sems"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row style="margin-top: 5px;" :gutter="5">
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="ay"
              placeholder="select Academic Year"
            >
              <el-option value="">select Academic Year</el-option>
              <el-option
                v-for="(item, index) in ays"
                :key="index"
                :label="item.ay"
                :value="item.ay"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="status"
              placeholder="select status"
            >
              <el-option value="">select status</el-option>
              <el-option
                v-for="(item, index) in statuses"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-col>

          <el-col :md="4">
            <el-button
              style="width:100%;"
              @click="search"
              size="small"
              type="success"
              >Search</el-button
            >
          </el-col>
          <el-col :md="4">
            <el-button
              style="width:100%;"
              @click="clear"
              size="small"
              type="primary"
              >all</el-button
            >
          </el-col>
        </el-row>
      </div>

      <hr />
      <v-client-table filterable="true" :columns="columns" :data="datas">
        <div slot="action" slot-scope="props">
          <router-link
            :to="{ name: 'enroll-details', params: { id: props.row.id } }"
            ><el-button type="success" size="small"
              >view</el-button
            ></router-link
          >
        </div>
      </v-client-table>
    </el-card>
  </div>
</template>

<style>
.semipolar-spinner,
.semipolar-spinner * {
  box-sizing: border-box;
}

.semipolar-spinner {
  position: fixed;
  z-index: 999;
  height: 5em;
  width: 5em;
  overflow: visible;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

.semipolar-spinner .ring {
  border-radius: 50%;
  position: absolute;
  border: calc(65px * 0.05) solid transparent;
  border-top-color: #ff1d5e;
  border-left-color: #ff1d5e;
  animation: semipolar-spinner-animation 2s infinite;
}

.semipolar-spinner .ring:nth-child(1) {
  height: calc(65px - 65px * 0.2 * 0);
  width: calc(65px - 65px * 0.2 * 0);
  top: calc(65px * 0.1 * 0);
  left: calc(65px * 0.1 * 0);
  animation-delay: calc(2000ms * 0.1 * 4);
  z-index: 5;
}

.semipolar-spinner .ring:nth-child(2) {
  height: calc(65px - 65px * 0.2 * 1);
  width: calc(65px - 65px * 0.2 * 1);
  top: calc(65px * 0.1 * 1);
  left: calc(65px * 0.1 * 1);
  animation-delay: calc(2000ms * 0.1 * 3);
  z-index: 4;
}

.semipolar-spinner .ring:nth-child(3) {
  height: calc(65px - 65px * 0.2 * 2);
  width: calc(65px - 65px * 0.2 * 2);
  top: calc(65px * 0.1 * 2);
  left: calc(65px * 0.1 * 2);
  animation-delay: calc(2000ms * 0.1 * 2);
  z-index: 3;
}

.semipolar-spinner .ring:nth-child(4) {
  height: calc(65px - 65px * 0.2 * 3);
  width: calc(65px - 65px * 0.2 * 3);
  top: calc(65px * 0.1 * 3);
  left: calc(65px * 0.1 * 3);
  animation-delay: calc(2000ms * 0.1 * 1);
  z-index: 2;
}

.semipolar-spinner .ring:nth-child(5) {
  height: calc(65px - 65px * 0.2 * 4);
  width: calc(65px - 65px * 0.2 * 4);
  top: calc(65px * 0.1 * 4);
  left: calc(65px * 0.1 * 4);
  animation-delay: calc(2000ms * 0.1 * 0);
  z-index: 1;
}

@keyframes semipolar-spinner-animation {
  50% {
    transform: rotate(360deg) scale(0.7);
  }
}
</style>

<script>
/* eslint-disable */

export default {
  data() {
    return {
      columns: [
        "student_id",
        "fullname",
        "course",
        "major",
        "semister",
        "year_level",
        "ac_year",
        "status",
        "action",
      ],
      datas: [],
      datastoFilter: [],
      isLoading: true,
      isLoadingStart:false,
      fullPage: false,
      ays: [],
      majors: [],
      courses: [],
      statuses: ["draft", "forwarded", "return for correction", "approved"],
      sems: ["1st", "2nd", "summer"],
      yearlevels: [],
      course: "",
      status: "",
      ay: "",
      major: "",
      sem: "",
    };
  },
  methods: {
    exportjson() {
      let jsondata = this.datas;

      var ws = XLSX.utils.json_to_sheet(this.datas, {
        header: [
          "student_id",
          "fullname",
          "course",
          "major",
          "semister",
          "year_level",
          "ac_year",
        ],
      });
      /* generate file and force a download*/
      var wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, "ws");
      XLSX.writeFile(wb, "sheetjs.xlsx");
      // console.log(ws)
    },
    clear() {
      this.course = "";
      this.status = "";
      this.ay = "";
      this.major = "";
      this.sem = "";
      this.datas = this.datastoFilter;
    },
    search() {
      if (this.major != "") {
        this.datas = this.datastoFilter.filter(
          (el) =>
            el.course == this.course &&
            el.major == this.major &&
            el.semister == this.sem &&
            el.ac_year == this.ay &&
            el.status == this.status
        );
      } else {
        this.datas = this.datastoFilter.filter(
          (el) =>
            el.course == this.course &&
            el.semister == this.sem &&
            el.ac_year == this.ay &&
            el.status == this.status
        );
      }
    },
  },
  created() {
    axios.get("/bccapi/yearlevels").then((res) => {
      this.yearlevels = res.data;
      // console.log(res.data)
    });
    axios.get("/bccapi/majors").then((res) => {
      this.majors = res.data;
      //  console.log(res.data)
    });
    axios.get("/bccapi/ays").then((res) => {
      this.ays = res.data;
      // console.log(res.data)
    });
    axios.get("/bccapi/courses").then((res) => {
      this.courses = res.data;
      //console.log(res.data)
    });

    axios.get("/bccapi/Api/enrollStudent/all/").then((res) => {
      //    this.datas=res.data
      this.isLoading = false;
      console.log(res.data);
      res.data.forEach((el) => {
        let ext_name = el.student.ext_name != null ? el.student.ext_name : "";
        let middle_name =
          el.student.middle_name != null ? el.student.middle_name : "";

        if (el.major != null) {
          this.datas.push({
            id: el.id,
            year_level: el.year_level.description,
            student_id: el.student.student_id,
            fullname: `${el.student.last_name}, ${el.student.first_name} ${middle_name} ${ext_name}`,
            course: el.course.code,
            major: el.major.name,
            semister: el.semister,
            ac_year: el.academic_year.ay,
            status: el.status,
            uri: `/bccapi/Admin/student/${el.id}/enroll`,
          });
        } else {
          this.datas.push({
            id: el.id,
            year_level: el.year_level.description,
            student_id: el.student.student_id,
            fullname: `${el.student.last_name}, ${el.student.first_name} ${middle_name} ${ext_name}`,
            course: el.course.code,
            major: null,
            semister: el.semister,
            ac_year: el.academic_year.ay,
            status: el.status,
            uri: `/bccapi/Admin/student/${el.id}/enroll`,
          });
        }
      });

      this.datastoFilter = this.datas;
    });
  },
};
</script>

<style></style>
