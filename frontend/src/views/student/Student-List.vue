<template>
  <div style="padding: 20px 20px;">
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
      <v-client-table :columns="columns" :data="students">
          <div slot="action" slot-scope="props">
          <router-link
            :to="{ name: 'student-edit', params: { id: props.row.id } }"
            ><el-button type="success" size="small"
              >view</el-button
            ></router-link
          >
        </div>
      </v-client-table>
    </el-card>
    <el-card>
      <v-client-table :columns="['id', 'fullname', 'action']" :data="ids">
        <!-- <a :href="props.row.uri" slot="action" slot-scope="props">
          <el-button
            type="success"
            size="small"
            circle
            icon="el-icon-edit"
          ></el-button
        ></a> -->
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
      columns: ["student_id", "fullname", "course", "action"],
      students: [],
      ids: [],
      isLoading: true,
      fullPage: false,
      courses: [],
    };
  },
  created() {
    console.log("nka abot");
    axios.get("/bccapi/courses").then((res) => {
      this.courses = res.data;
    });
    axios.get("/bccapi/ids").then((res) => {
      this.ids = res.data;
      this.ids.forEach((el) => {
        (el.fullname = `${el.last_name}, ${el.first_name}`),
          (el.uri = "/editIDs/" + el.id);
      });
    });
    axios.get("/bccapi/students").then((res) => {
      this.students = res.data;
      this.isLoading = false;
      res.data.forEach((el) => {
        let ext_name = el.ext_name != null ? el.ext_name : "";
        let course = this.courses.find((e) => e.id == el.course);
        el.fullname = `${el.last_name}, ${el.first_name} ${ext_name}`;
        el.course = course.code;
        el.uri = "/editStudent/" + el.id;
      });
    });
  },
};
</script>
