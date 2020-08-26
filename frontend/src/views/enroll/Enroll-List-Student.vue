<template>
<el-card>
  <v-client-table filterable="true" :columns="columns" :data="datas">
    <div slot="action" slot-scope="props">
      <router-link
        :to="{ name: 'enroll-student-details', params: { id: props.row.id } }"
        ><el-button type="success" size="small">view</el-button></router-link
      >
    </div>
  </v-client-table>
</el-card>

</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      columns: [
        "student.first_name",
          "student.last_name",
        "course.code",
        "semister",
        "year_level.code",
        "academic_year.ay",
        "status",
        "action",
      ],
      datas: [],
      datastoFilter: [],
      isLoading: true,
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
  methods: {},
  async created() {


    let accessToken = this.$store.getters.currentUser.access;
    let responseUser = await axios.post("/bccapi/token/user/", {
      token: accessToken,
    });
    let responseUserStudent = await axios.get("/bccapi/studentusers");
    if (
      responseUserStudent.data.filter((el) => el.user == responseUser.data.id)
        .length > 0
    ) {
      let isStudentExistResponse = await axios.get(
        `/bccapi/getstudentbyid/${
          responseUserStudent.data.find((el) => el.user == responseUser.data.id)
            .student_id
        }`
      );

      axios
        .get("/bccapi/enrollStudentbystudent/" + isStudentExistResponse.data.id)
        .then((response) => {
          this.isLoading = false;
     
          response.data.forEach((el) => {
            axios.get("/bccapi/students/" + el.student).then((res) => {
              console.log(res.data)
              el.fullname = res.data.first_name;
            });
          });
          this.datas = response.data;
        });
    }
  },
};
</script>

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
