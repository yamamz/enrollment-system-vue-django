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
                :disabled="
                  enroll.course == '' ||
                    enroll.course == 4 ||
                    enroll.course == 5 ||
                    enroll.course == 3
                "
                filterable
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
            :disabled="
              enroll.status == 'forwarded' ||
                enroll.course == '' ||
                enroll.semister == '' ||
                enroll.year_level == '' ||
                enroll.academic_year == ''
            "
            style="float: right;"
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
              v-model="subject"
              label="full"
              value="id"
              :options="subjects"
            ></v-select>
          </el-col>
          <el-col :md="4">
            <el-button
              :disabled="enroll.status == 'forwarded'"
              size="small"
              @click="addSubject"
              style="width: 100%;"
              type="primary"
              >add</el-button
            >
          </el-col>
        </el-row>
        <hr />

        <el-table :data="enroll.enroll_subjects" style="width: 100%">
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
                  deleteRow(scope.$index, enroll.enroll_subjects)
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
            enroll.status == 'forwarded' ||
              enroll.course == '' ||
              enroll.semister == '' ||
              enroll.year_level == '' ||
              enroll.academic_year == '' ||
              enroll.enroll_subjects.length == 0
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

      enroll: {
        student: "",
        course: "",
        major: null,
        academic_year: "",
        year_level: "",
        semister: "",
        status: "draft",
        enroll_subjects: [],
      },
    };
  },
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    addSubject() {
      //let subject=this.subjects.find(el=>el.id == this.subject.id)

      console.log(this.subject);

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
      let major = this.enroll.major != null ? this.enroll.major : "0";

      axios
        .get(
          `/bccapi/searchenrolllist/${this.enroll.student}/${this.enroll.course}/${major}/${this.enroll.semister}/${this.enroll.year_level}/${this.enroll.academic_year}`
        )
        .then((res) => {
          if (res.data.length == 0) {
            this.enroll.enroll_subjects.forEach((el) => {
              el.status = "forwarded";
            });
            this.enroll.status = "forwarded";
            axios.post("/bccapi/enrolls/", this.enroll).then((result) => {
              this.$notify({
                title: "Info",
                message: "Forward Successfully",
                type: "success",
              });
            });
          } else {
            this.$notify({
                title: "Oops...",
                message: "already save on this semister. You will be redirected to the list of your enrolled data",
                type: "error",
              });
            
            setTimeout(() => { }, 3000);


          }
        });
    },
    getSubjects() {
      let major = this.enroll.major != null ? this.enroll.major : "0";
      axios
        .get(
          `/bccapi/Apiaddsubjectbycuriculum/${this.enroll.course}/${major}/${this.enroll.semister}/${this.enroll.year_level}`
        )
        .then((res) => {
          console.log(res.data);
          this.enroll.enroll_subjects = [];
          res.data.forEach((el) => {
            this.enroll.enroll_subjects.push({
              grade_status: null,
              grade: null,
              status: "draft",
              subject: el.id,
              instructor: null,
              sub: el,
            });
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
      this.ays = res.data.filter((e) => e.status == true);
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
    axios.get("/bccapi/students/" + this.$route.params.id).then((res) => {
      this.students.push(res.data);
      this.students.forEach((el) => {
        el.fullname = `${el.last_name}, ${el.first_name}`;
      });

      this.enroll.student = this.$route.params.id;
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
