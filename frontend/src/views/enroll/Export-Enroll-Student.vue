<template>
  <div style="padding: 10px;" id="app">
    <el-card>
      <h4>Enrolled Student by Course</h4>
      <hr />
      <h6>Search Parameters</h6>
      <el-row :gutter="5">
        <el-col :md="6">
          <el-select
            size="small"
            style="width: 100%;"
            v-model="course"
            placeholder="course"
          >
            <el-option
              v-for="(item, index) in courses"
              :value="item.id"
              :label="item.code"
              :key="index"
            ></el-option>
          </el-select>
        </el-col>

        <el-col :md="6">
          <el-select
            size="small"
            style="width: 100%;"
            v-model="ay"
            placeholder="academic year"
          >
            <el-option
              v-for="(item, index) in ays"
              :value="item.id"
              :label="item.ay"
              :key="index"
            ></el-option>
          </el-select>
        </el-col>

        <el-col :md="6">
          <el-select
            size="small"
            style="width: 100%;"
            v-model="sem"
            placeholder="semister"
          >
            <el-option
              v-for="(item, index) in semisters"
              :value="item"
              :label="item"
              :key="index"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :md="6">
          <el-button
            :loading="isLoading"
            @click="search"
            :disabled="
              subjects.length == 0 || sem == '' || course == '' || ay == ''
            "
            size="small"
            style="width: 100%;"
            type="danger"
            >Search</el-button
          >
        </el-col>
      </el-row>
      <hr />

      <v-client-table filterable="true" :columns="columns" :data="datas">
      </v-client-table>
      <el-button type="primary" size="small" @click="exportexcel"
        >export to excel</el-button
      >
    </el-card>
  </div>
</template>

<script>
/* eslint-disable */
import { read, write, utils, writeFile } from 'xlsx'
export default {
     data() {
      return {
        datas: [],
        course: "",
        sem: "",
        isLoading: false,
        ay: "",
        aosf: null,
        columns: [
          "student_id",
          "fullname",
          "course",
          "major",
          "semister",
          "year_level",
          "ac_year",
        ],
        courses: [],
        ays: [],
        semisters: ["1st", "2nd", "summer"],
        datatoExport: [],

        subjects: [],
      };
    },
    methods: {
      exportexcel() {
        let jsondata = this.datatoExport;


        var ws = utils.json_to_sheet(jsondata, {
          header: [
            "student_id",
            "lastname",
            "firstname",
            "middlename",
            "extension",
            "gender",
            "address",
            "birthdate",
            "course",
            "year_level",
            "zip_code",
            "email",
            "lrn",
            "mobile",
            "subject",
            "desc",
            "unit",
            "grade",
            "units",
            "codes",
            "descriptions",
          ],
          skipHeader: false,
        });
        /* generate file and force a download*/
        var wb = utils.book_new();
        utils.book_append_sheet(wb, ws, "ws");
      writeFile(wb, "report.xlsx");
      },
      async search() {
        try {
          this.isLoading = true;
          let res = await axios.get(
            `/bccapi/Api/enrollStudent/${this.ay}/${this.course}/${this.sem}/`
          );
          this.datas = [];
          this.datatoExport = [];
          this.isLoading = false;
          res.data.forEach((el) => {
            let ext_name =
              el.student.ext_name != null ? el.student.ext_name : "";
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
                uri: `/Admin/student/${el.id}/enroll`,
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
                uri: `/Admin/student/${el.id}/enroll`,
              });
            }
            let total_units = 0;
            let subject_codes = "";
            let subject_descriptions = "";
            let totalLab = 0;
            el.enroll_subjects.forEach((e, index) => {
              if (e.status == "enrolled") {
                console.log(e);
                let subject = this.subjects.find((sub) => sub.id === e.subject);
                total_units = total_units + subject.unit;
                if (index + 1 != el.enroll_subjects.length) {
                  subject_descriptions =
                    subject_descriptions + `${subject.description}, `;
                  subject_codes = subject_codes + `${subject.code}, `;
                } else {
                  subject_descriptions =
                    subject_descriptions + `${subject.description}`;
                  subject_codes = subject_codes + `${subject.code}`;
                }
                if (subject.description.toUpperCase().includes("LAB")) {
                  totalLab =
                    parseFloat(totalLab) +
                    parseFloat(this.aosf[0].laboratory_fees);
                }
              }
            });
            let lrn = el.student.lrn_num != null ? el.student.lrn_num : "";
            let major = el.major != null ? el.major.description : "";
            let student_id_fee =
              el.year_level.code == "1st" && el.semister == "1st"
                ? this.aosf[0].school_id_fees
                : "0.00";

            let intrance_fee =
              el.year_level.code == "1st" && el.semister == "1st"
                ? this.aosf[0].entrance_exam
                : "0.00";
            let student_hand_book =
              el.year_level.code == "1st" && el.semister == "1st"
                ? this.aosf[0].handbook_fees
                : "0.00";
            let insurance =
              el.semister == "1st" ? this.aosf[0].insurance : "0.00";
            this.datatoExport.push({
             student_id: el.student.student_id,
              lastname: el.student.last_name,
              firstname: el.student.first_name,
              middlename: el.student.middle_name,
              extension: el.student.ext_name,
              gender: el.student.gender,
              address: `${el.student.address!=null?el.student.address: `${el.student.street} ${el.student.brgy}`}, ${el.student.city}, ${el.student.province}`,
              birthdate: new Date(el.student.birth_date).toDateString(),
              course: `${el.course.code} ${major}`,
              year_level: el.year_level.description,
              zip_code: el.student.zip_code,
              email: el.student.email_add,
              lrn: lrn,
              mobile: el.student.mobile_no,
              units: total_units,
              codes: subject_codes,
              descriptions: subject_descriptions,
              entrance_exam: intrance_fee,
              athletic_fee: this.aosf[0].athletic_fees,
              internet_fee: this.aosf[0].internet_fees,
              laborator_fee:
                el.course.code != "BSIT" ? totalLab.toFixed(2) : "0.00",
              development_fee: this.aosf[0].development_fee,
              guidance_fee: this.aosf[0].guidance_fees,
              student_handbook: student_hand_book,
              computer_laboratory:
                el.course.code == "BSIT" ? totalLab.toFixed(2) : "0.00",
              library_fee: this.aosf[0].library_fee,
              medical_fee: this.aosf[0].medical_and_dental_fees,
              registration_free: this.aosf[0].registration_fees,
              insurance_fee: insurance,
              cultural_fee: this.aosf[0].cultural_fees,
            });

              el.enroll_subjects.forEach((e, index) => {
              if (e.status == "enrolled") {
                   let subject = this.subjects.find((sub) => sub.id === e.subject);
                   this.datatoExport.push({
                     subject:subject.code,
                     desc:subject.description,
                     unit:subject.unit,
                     grade:e.grade != null ? e.grade : (e.grade_status != null? e.grade_status : '')
                   })
              }
            });
          });
        } catch (err) {
          console.log(err);
        }
      },
    },

    async created() {
      let resCourse = await axios.get("/bccapi/courses");
      this.courses = resCourse.data;

      let resAy = await axios.get("/bccapi/ays");
      this.ays = resAy.data;
      let ressub = await axios.get("/bccapi/subjects");
      this.subjects = ressub.data;

      axios.get("/bccapi/aosfs").then((res) => {
        console.log(res.data)
        this.aosf = res.data;
      });
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
