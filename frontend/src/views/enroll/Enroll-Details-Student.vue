<template>
  <div id="app">
    <el-form :ref="enroll" :model="enroll" size="small" label-position="top">
      <el-card>
        <h6>Enrollment Form</h6>
        <br />
        <el-row :gutter="5">
          <el-col :md="8">
            <el-form-item label="Fullname">
              <el-select
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                filterable
                style="width: 100%;"
                placeholder="select a student"
                v-model="enroll.student"
              >
                <el-option
                  v-for="(item, index) in students"
                  :label="item.fullname"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="8">
            <el-form-item label="Course">
              <el-select
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                placeholder="select a course"
                style="width: 100%;"
                v-model="enroll.course"
              >
                <el-option
                  v-for="(item, index) in courses"
                  :label="item.code"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="8">
            <el-form-item label="Major">
              <el-select
                filterable
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                style="width: 100%;"
                placeholder="select a major"
                v-model="enroll.major"
              >
                <el-option
                  v-for="(item, index) in majors"
                  :label="item.name"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="8">
            <el-form-item label="Year Level">
              <el-select
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                placeholder="select a year level"
                style="width: 100%;"
                v-model="enroll.year_level"
              >
                <el-option
                  v-for="(item, index) in yearlevels"
                  :label="item.description"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="8">
            <el-form-item label="Semister">
              <el-select
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                placeholder="select a semister"
                style="width: 100%;"
                v-model="enroll.semister"
              >
                <el-option
                  v-for="(item, index) in semisters"
                  :label="item"
                  :value="item"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="8">
            <el-form-item label="Academic Year">
              <el-select
                :disabled="
                  enroll.status == 'forwarded' || enroll.status == 'approved'
                "
                placeholder="select academic year"
                style="width: 100%;"
                v-model="enroll.academic_year"
              >
                <el-option
                  v-for="(item, index) in ays"
                  :label="item.ay"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>
      <el-card>
        <div slot="header" class="clearfix">
          <span>Subjects</span>
          <el-button
            style="float: right;"
            :disabled="
              enroll.status == 'forwarded' || enroll.status == 'approved'
            "
            @click="getSubjects"
            size="small"
            round
            type="danger"
            >Add Subjects on curriculum</el-button
          >
        </div>

        <el-row :gutter="10">
          <el-col :md="20">
            <v-select
              :disabled="
                enroll.status == 'forwarded' || enroll.status == 'approved'
              "
              v-model="subject"
              label="full"
              value="id"
              :options="subjects"
            ></v-select>
          </el-col>
          <el-col :md="4">
            <el-button
              size="small"
              :disabled="
                enroll.status == 'forwarded' || enroll.status == 'approved'
              "
              @click="addSubject"
              style="width: 100%;"
              type="primary"
              >add</el-button
            >
          </el-col>
        </el-row>
        <hr />

        <el-table
          v-loading="loading"
          element-loading-text="Loading..."
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.1)"
          :data="enroll.enroll_subjects"
          style="width: 100%"
        >
          <el-table-column prop="sub.code" label="Code" width="100">
          </el-table-column>
          <el-table-column prop="sub.description" label="Descriptive Title">
          </el-table-column>
          <el-table-column prop="sub.unit" label="Unit"> </el-table-column>
          <el-table-column prop="status" label="status"> </el-table-column>

          <el-table-column label="action" width="120">
            <template slot-scope="scope">
              <el-button
                :disabled="scope.row.status == 'forwarded'"
                @click.native.prevent="
                  deleteRow(scope.$index, enroll.enroll_subjects, scope.row.id)
                "
                type="danger"
                size="small"
              >
                Remove
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <br />
        <el-button
          :disabled="
            enroll.status == 'forwarded' || enroll.status == 'approved'
          "
          @click="save"
          size="small"
          type="success"
          >forward for approval</el-button
        >
      </el-card>
    </el-form>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      students: [],
      ays: [],
      majors: [],
      courses: [],
      subject: null,
      instructors: [],
      subjects: [],
      yearlevels: [],
      semisters: ["1st", "2nd", "summer"],
      loading: true,

      enroll: {
        student: "",
        course: null,
        major: null,
        academic_year: null,
        year_level: null,
        semister: "",
        status: "forwarded",
        enroll_subjects: [],
      },
    };
  },
  methods: {
    deleteRow(index, rows, id) {
      if (rows[index].status != "draft") {
        axios.delete("/bccapi/subjectsenrolled/" + id + "/").then((res) => {
          console.log(res.data);
          rows.splice(index, 1);
        });
      } else {
        rows.splice(index, 1);
      }
    },
    addSubject() {
      if (
        this.enroll.enroll_subjects.find((e) => e.subject == this.subject) ==
        null
      ) {
        this.enroll.enroll_subjects.push({
          grade_status: null,
          grade: null,
          status: "draft",
          subject: this.subject.id,
          instructor: null,
          sub: this.subject,
        });
      }
    },
    save() {
      this.enroll.status = "forwarded";
      this.enroll.enroll_subjects.forEach((el) => {
        el.status = "forwarded";
      });
      axios
        .put("/bccapi/enrolls/" + this.enroll.id + "/", this.enroll)
        .then((result) => {
          //window.location.replace(`/student/${result.data.id}/enroll/`);
          this.$notify({
            title: "Success",
            message: "Forward Successfully",
            type: "success",
          });
        });
    },
    getSubjects() {
      let major = this.enroll.major != null ? this.enroll.major : "0";
      axios
        .get(
          `/bccapi/Apiaddsubjectbycuriculum/${this.enroll.course}/${major}/${this.enroll.semister}/${this.enroll.year_level}`
        )
        .then((res) => {
          res.data.forEach((el) => {
            if (
              this.enroll.enroll_subjects.find((e) => e.subject == el.id) ==
              null
            ) {
              this.enroll.enroll_subjects.push({
                grade_status: null,
                grade: null,
                status: "draft",
                subject: el.id,
                instructor: null,
                sub: el,
              });
            } else {
              console.log("already added");
            }
          });
        })
        .catch((err) => {
          this.$message.error("Oops, No Curriculum added on this parameters");
        });
    },
  },
  created() {
    axios.get("/bccapi/curriculumss").then((res) => {
      res.data.forEach((el) => {
        el.subjects.forEach((e) => {
          if (this.subjects.find((sub) => sub.id == e.id) == null) {
            this.subjects.push(e);
          }
        });
      });

      this.subjects.forEach((el) => {
        el.full = `${el.code}-${el.description}`;
      });

      axios.get("/bccapi/enrolls/" + this.$route.params.id).then((ress) => {
        this.enroll = ress.data;
        console.log(this.enroll);

        this.enroll.enroll_subjects.forEach((el) => {
          let subject = this.subjects.find((e) => e.id == el.subject);
          console.log(subject);
          el.sub = subject;
        });

        this.loading = false;

        axios.get("/bccapi/students/" + this.enroll.student).then((ress) => {
          this.students.push(ress.data);
          this.students.forEach((el) => {
            el.fullname = `${el.last_name}, ${el.first_name}`;
          });
        });
      });
    });

    axios.get("/bccapi/instructors").then((res) => {
      this.instructors = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/majors").then((res) => {
      this.majors = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/ays").then((res) => {
      this.ays = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/courses").then((res) => {
      this.courses = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/yearlevels").then((res) => {
      this.yearlevels = res.data;
      console.log(res.data);
    });
  },
};
</script>

<style>
.el-form-item--small .el-form-item__content,
.el-form-item--small .el-form-item__label {
  line-height: 0px;
}

.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
  background: #dfe5fb;
  border: none;
  color: #394066;
  text-transform: lowercase;
  font-variant: small-caps;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: #394066;
}
</style>
