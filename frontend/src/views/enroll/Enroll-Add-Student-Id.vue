<template>
  <div>
    <el-row justify="center">
      <el-col :lg="8">
        <el-card>
          <el-form size="small" :ref="form" :model="form">
            <el-row>
              <el-col>
                <el-form-item label="Student Id">
                  <el-input
                    placeholder=" input your student id"
                    size="small"
                    v-model="form.student_id"
                  ></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-button
                :disabled="form.student_id == ''"
                type="primary"
                @click="save()"
                size="small"
                >Go</el-button
              >
            </el-row>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      form: {
        student_id: "",
        user: "",
      },
    };
  },
  methods: {
    async save() {
      let isStudentExistResponse = await axios.get(
        `/bccapi/getstudentbyid/${this.form.student_id}`
      );
      if (isStudentExistResponse.data.is_exists) {
        try {
          let response = await axios.post("/bccapi/studentusers/", this.form);
          this.$router.push({
            name: "enroll-student",
            params: { id: this.form.user },
          });
        } catch (e) {
          console.log(e);
        }
      }
    },
  },
  async created() {
    let accessToken = this.$store.getters.currentUser.access;
    let responseUser = await axios.post("/bccapi/token/user/", {
      token: accessToken,
    });
    this.form.user = responseUser.data.id;
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
      this.$router.push({
        name: "enroll-student",
        params: { id: isStudentExistResponse.data.id },
      });
    }
  },
};
</script>

<style></style>
