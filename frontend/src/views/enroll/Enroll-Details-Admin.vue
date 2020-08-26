<template>
  <div>
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
              v-model="subject"
              label="full"
              value="id"
              :options="subjects"
            ></v-select>
          </el-col>
          <el-col :md="4">
            <el-button
              size="small"
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
                v-show="
                  scope.row.status == 'forwarded' ||
                    scope.row.status == 'returned for correction'
                "
                :disabled="scope.row.status == 'forwarded'"
                @click.native.prevent="
                  deleteRow(scope.$index, enroll.enroll_subjects, scope.row.id)
                "
                type="danger"
                size="small"
              >
                Remove
              </el-button>
              <el-button
                v-show="scope.row.status == 'enrolled'"
                :disabled="scope.row.status == 'drop'"
                @click="drop(scope.row.id)"
                type="danger"
                size="small"
              >
                drop
              </el-button>
              <el-button
                v-show="scope.row.status == 'drop'"
                @click="enrolldrop(scope.row.id)"
                type="success"
                size="small"
              >
                enroll
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <br />
        <el-row :gutter="5">
          <el-col :md="2">
            <el-button
              style="width:100%;"
              :disabled="enroll.status == 'returned for correction'"
              @click="save"
              size="small"
              type="primary"
              >enroll</el-button
            >
          </el-col>
          <el-col :md="2">
            <el-button
              style="width:100%;"
              :disabled="
                enroll.status == 'widrawed' ||
                  enroll.status == 'forwarded' ||
                  enroll.status == 'returned for correction'
              "
              size="small"
              type="success"
              @click="prints"
              >print</el-button
            >
          </el-col>
          <el-col :md="17">
            <el-button
              :disabled="
                enroll.status == 'widrawed' ||
                  enroll.status == 'widraw' ||
                  enroll.status == 'approved' ||
                  enroll.status == 'returned for correction'
              "
              @click="returned"
              size="small"
              type="warning"
              >returned for correction</el-button
            >
          </el-col>

          <el-col :md="3">
            <el-button
              :disabled="
                enroll.status == 'widrawed' ||
                  enroll.status == 'forwarded' ||
                  enroll.status == 'returned for correction'
              "
              @click="widraw"
              size="small"
              type="danger"
              >widraw enrollment</el-button
            >
          </el-col>
        </el-row>
      </el-card>
    </el-form>
  </div>
</template>

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

<script>
/* eslint-disable */
import pdfMake from "pdfmake/build/pdfmake";
import pdfFonts from "pdfmake/build/vfs_fonts";
import {imageString} from "../../helper/image";
pdfMake.vfs = pdfFonts.pdfMake.vfs;
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
      index: "",
      aosf: null,
      student_id: this.$route.params.id,

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
    prints() {
      console.log("print");
      let totalunit = 0;

      let totalLab = 0;
      let student = this.students.find((el) => el.id == this.enroll.student);
      let course = this.courses.find((e) => e.id == this.enroll.course);
      let major = this.majors.find((e) => e.id == this.enroll.major);
      let ay = this.ays.find((e) => e.id == this.enroll.academic_year);
      let year = this.yearlevels.find((e) => e.id == this.enroll.year_level);
      console.log(major);

      this.enroll.enroll_subjects.forEach((el) => {
        if (el.status == "enrolled") {
          totalunit = totalunit + el.sub.unit;

          if (el.sub.description.toUpperCase().includes("LAB")) {
            console.log("1");
            totalLab =
              parseFloat(totalLab) + parseFloat(this.aosf[0].laboratory_fees);
          }
        }
      });
      //let year=
      let student_id_fee =
        year.code == "1st" && this.enroll.semister == "1st"
          ? this.aosf[0].school_id_fees
          : "0.00";

      let intrance_fee =
        year.code == "1st" && this.enroll.semister == "1st"
          ? this.aosf[0].entrance_exam
          : "0.00";
      let student_hand_book =
        year.code == "1st" && this.enroll.semister == "1st"
          ? this.aosf[0].handbook_fees
          : "0.00";
      let insurance =
        this.enroll.semister == "1st" ? this.aosf[0].insurance : "0.00";

      let totalTuition = this.aosf[0].tution_fee_ammount * totalunit;
      let totalAOSF =
        parseFloat(this.aosf[0].athletic_fees) +
        parseFloat(this.aosf[0].internet_fees) +
        parseFloat(this.aosf[0].cultural_fees) +
        parseFloat(this.aosf[0].guidance_fees) +
        parseFloat(student_hand_book) +
        parseFloat(this.aosf[0].medical_and_dental_fees) +
        parseFloat(this.aosf[0].registration_fees) +
        parseFloat(intrance_fee) +
        parseFloat(student_id_fee) +
        parseFloat(this.aosf[0].development_fee) +
        parseFloat(this.aosf[0].library_fee) +
        parseFloat(insurance) +
        parseFloat(totalLab);

      let totalBilling = totalTuition + totalAOSF;
      {
        var dd = {
          pageOrientation: "portrait",

          content: [
            {
              margin: [0, 0, 0, 10],
              columns: [
                {
                  width: "auto",
                  margin: [100, 0, 0, 0],
                  stack: [
                    {
                      width: 50,
                      height: 50,
                      image:imageString.image,
                    },
                  ],
                },
                {
                  width: 250,
                  alignment: "center",
                  text: [
                    {
                      text: "BUENAVISTA COMMUNITY COLLEGE ",
                      fontSize: 14,
                      bold: true,
                    },
                    "\n Cangawa, Buenavista, Bohol",
                    " \n Telefax: (038)5139169/Tel.: 513-9179",
                    {
                      text: "\n CERTIFICATE OF REGISTRATION",
                      bold: true,
                      fontSize: 13,
                    },
                  ],
                },
              ],
            },
            {
              columns: [
                {
                  width: 240,
                  fontSize: 10,
                  text: [
                    {
                      text: `FULLNAME: `,
                      bold: true,
                    },
                    `${student.last_name}, ${student.first_name} ${
                      student.middle_name != null ? student.middle_name : ""
                    } ${student.ext_name != null ? student.ext_name : ""}`,
                  ],
                },
                {
                  fontSize: 10,
                  width: 150,
                  text: [
                    {
                      text: `STUDENT ID No.: `,
                      bold: true,
                    },
                    `${student.student_id}`,
                  ],
                },
                {
                  fontSize: 10,
                  width: 200,
                  text: [
                    {
                      text: `GENDER: `,
                      bold: true,
                    },
                    student.gender,
                  ],
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,
                  width: 240,
                  text: [
                    {
                      text: `ACADEMIC YEAR: `,
                      bold: true,
                    },
                    ay.ay,
                  ],
                },
                {
                  fontSize: 10,
                  width: 150,
                  text: [
                    {
                      text: `TERM: `,
                      bold: true,
                    },
                    this.enroll.semister == "summer"
                      ? this.enroll.semister
                      : this.enroll.semister + " SEMESTER",
                  ],
                },
                {
                  fontSize: 10,
                  width: 200,
                  text: [
                    {
                      text: `DATE: `,
                      bold: true,
                    },
                    `${new Date().toDateString()}`,
                  ],
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,
                  width: 240,
                  text: [
                    {
                      text: `YEAR LEVEL: `,
                      bold: true,
                    },
                    year.description,
                  ],
                },
                {
                  fontSize: 10,
                  width: 150,
                  text: [
                    {
                      text: `COURSE: `,
                      bold: true,
                    },
                    course.code,
                  ],
                },
                {
                  fontSize: 10,
                  width: 150,
                  text: [
                    {
                      text: `MAJOR: `,
                      bold: true,
                    },
                    major != null ? major.name : "None",
                  ],
                },
              ],
            },

            {
              style: "tableExample",
              layout: "noBorders",
              table: {
                widths: [80, 350, 40],
                body: [
                  [
                    {
                      text: "Subject Code",
                      bold: true,
                      style: "tableHeader",
                    },
                    {
                      text: "Subject Description",
                      bold: true,
                      style: "tableHeader",
                    },

                    {
                      text: "Units",
                      alignment: "center",
                      bold: true,
                      style: "tableHeader",
                    },
                  ],
                ],
              },
              layout: {
                hLineWidth: function(i, node) {
                  return i === 1 || i === node.table.body.length ? 1 : 0.0;
                },
                vLineWidth: function(i, node) {
                  return i === 0 || i === node.table.widths.length ? 0.0 : 0.0;
                },

                vLineColor: function(i, node) {
                  return i === 0 || i === node.table.widths.length
                    ? "black"
                    : "gray";
                },
              },
            },
            {
              columns: [
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 472,
                  text: "Total # of Units: " + totalunit,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0, 0, 0],
                  width: 500,
                  bold: true,
                  text:
                    "______________________________________________________________________________________________________________",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0],
                  width: 50,
                  text: "Tuition Fee:\n",
                },
                {
                  bold: true,
                  fontSize: 10,
                  alignment: "center",
                  margin: [0, 0],
                  width: 150,
                  text: "No. of Units Earned \n" + totalunit,
                },
                {
                  bold: true,
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 120,
                  text: "Amount / Unit \n" + this.aosf[0].tution_fee_ammount,
                },
                {
                  bold: true,
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: "Total \n" + totalTuition.toFixed(2),
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0, 0, 0],
                  width: 500,
                  bold: true,
                  text:
                    "______________________________________________________________________________________________________________",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0],
                  width: 150,
                  text: "\n",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0],
                  width: 150,
                  text: "Miscellaneous Fee:\n",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tEntrance Exam",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text:
                    year.code == "1st" && this.enroll.semister == "1st"
                      ? this.aosf[0].entrance_exam
                      : "0.0",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tAthletic fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].athletic_fees,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tInternet fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].internet_fees,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tLaboratory fee(none computer subject)",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: course.code != "BSIT" ? totalLab.toFixed(2) : "0.00",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tDevelopment fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].development_fee,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tGuidance fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].guidance_fees,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tStudent Handbook",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text:
                    year.code == "1st" && this.enroll.semister == "1st"
                      ? this.aosf[0].handbook_fees
                      : "0.00",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tComputer Lab. Fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: course.code == "BSIT" ? totalLab.toFixed(2) : "0.00",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tLibrary Fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].library_fee,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tMedical/Dental Fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].medical_and_dental_fees,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tStudent ID",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text:
                    year.code == "1st" && this.enroll.semister == "1st"
                      ? this.aosf[0].school_id_fees
                      : "0.00",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tRegistration Fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].registration_fees,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tInsurance",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text:
                    this.enroll.semister == "1st"
                      ? this.aosf[0].insurance
                      : "0.00",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "\tCultural Fee",
                },
                {
                  fontSize: 10,
                  alignment: "right",
                  margin: [0, 0],
                  width: 150,
                  text: this.aosf[0].cultural_fees,
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0],
                  alignment: "right",
                  width: 464,
                  text: totalAOSF.toFixed(2),
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0, 0, 0],
                  width: 500,
                  bold: true,
                  text:
                    "______________________________________________________________________________________________________________",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0, 0, 0],
                  alignment: "left",
                  width: 64,
                  text: "Total Billing",
                },
                {
                  fontSize: 10,
                  bold: true,
                  margin: [0, 0, 0, 0],
                  alignment: "right",
                  width: 400,
                  text: totalBilling.toFixed(2), //.toLocaleString(undefined, {maximumFractionDigits:2})
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0, 0, 0],
                  width: 500,
                  bold: true,
                  text:
                    "______________________________________________________________________________________________________________",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  width: 500,
                  bold: true,
                  text: "",
                },
              ],
            },

            {
              columns: [
                {
                  fontSize: 10,
                  alignment: "left",
                  margin: [10, 10],
                  width: 350,
                  text: "Checked by: \n",
                },
                {
                  fontSize: 10,
                  margin: [0, 10],
                  width: "*",
                  text: `Approved by: \n`,
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,

                  margin: [0, 0],
                  alignment: "left",
                  width: 170,
                  text: "",
                },
              ],
            },
            {
              columns: [
                {
                  fontSize: 10,
                  bold: true,
                  alignment: "left",
                  margin: [30, 10],
                  width: 350,
                  text: "JUDITHO A. BAUTISTA \n            Asst. Registrar",
                },
                {
                  fontSize: 10,
                  bold: true,
                  margin: [20, 10],
                  width: "*",
                  text: `MA. MAY N. CUPTA \n                   Registrar`,
                },
              ],
            },
          ],

          styles: {
            header: {
              fontSize: 30,
              bold: true,
              alignment: "left",
              margin: [0, 0, 0, 20],
            },
            subheader: {
              fontSize: 16,
            },
            tableExample: {
              margin: [0, 5, 0, 15],
            },
            tableHeader: {
              bold: true,
              fontSize: 11,
              color: "black",
            },
          },
          defaultStyle: {
            // alignment: 'justify'
          },
        };

        this.enroll.enroll_subjects.forEach((el) => {
          if (el.status == "enrolled") {
            dd.content[4].table.body.push([
              {
                text: el.sub.code,
                fontSize: 9,
              },
              {
                text: el.sub.description,
                fontSize: 9,
              },

              {
                text: el.sub.unit,
                fontSize: 9,
                alignment: "center",
              },
            ]);
          }
        });

        pdfMake.createPdf(dd).open();
      }
    },
    widraw() {
      this.enroll.status = "widrawed";
      this.enroll.enroll_subjects.forEach((el) => {
        el.status = "widrawed";
      });
      axios
        .put("/bccapi/enrolls/" + this.enroll.id + "/", this.enroll)
        .then((result) => {
          this.$notify({
            title: "Success",
            message: "widraw Successfully",
            type: "success",
          });
        })
        .catch((err) => {
          this.enroll.status = "approved";
          this.enroll.enroll_subjects.forEach((el) => {
            el.status = "enrolled";
          });
        });
    },
    print() {},
    drop(id) {
      console.log("drop");
      axios
        .post(`/bccapi/Api/${id}/enroll/subjects/drop/`)
        .then((res) => {
          this.index = this.enroll.enroll_subjects.findIndex((e) => e.id == id);
          this.enroll.enroll_subjects[this.index].status = "drop";
        })
        .catch((err) => {
          console.log(err);
        });
    },
    enrolldrop(id) {
      console.log("drop");
      axios
        .post(`/bccapi/Api/${id}/enroll/subjects/enroll/`)
        .then((res) => {
          this.index = this.enroll.enroll_subjects.findIndex((e) => e.id == id);
          this.enroll.enroll_subjects[this.index].status = "enrolled";
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteRow(index, rows, id) {
      axios.delete("/bccapi/subjectsenrolled/" + id + "/").then((res) => {
        console.log(res.data);
        rows.splice(index, 1);
      });
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
      console.log(this.enroll);
      this.enroll.status = "approved";
      this.enroll.enroll_subjects.forEach((el) => {
        if (el.status != "drop") {
          el.status = "enrolled";
        }
      });
      axios
        .put("/bccapi/enrolls/" + this.enroll.id + "/", this.enroll)
        .then((result) => {
          this.$notify({
            title: "Success",
            message: "enrolled Successfully",
            type: "success",
          });

          this.refresh();
        })
        .catch((err) => {
          this.enroll.status = "forwarded";
          this.enroll.enroll_subjects.forEach((el) => {
            el.status = "forwarded";
          });
        });
    },
    refresh() {
      axios.get("/bccapi/enrolls/" + this.student_id).then((ress) => {
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
    },
    returned() {
      this.enroll.status = "returned for correction";
      this.enroll.enroll_subjects.forEach((el) => {
        el.status = "returned for correction";
      });
      axios
        .put("/bccapi/enrolls/" + this.enroll.id + "/", this.enroll)
        .then((result) => {
          this.$notify({
            title: "Success",
            message: "return Successfully",
            type: "success",
          });
        })
        .catch((err) => {
          this.enroll.status = "forwarded";
          this.enroll.enroll_subjects.forEach((el) => {
            el.status = "forwarded";
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
          console.log(res.data);
          //this.enroll.enroll_subjects=[]
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
    axios.get("/bccapi/subjects").then((res) => {
      res.data.forEach((el) => {
        if (this.subjects.find((sub) => sub.id == el.id) == null) {
          el.uri = `subjects/${el.id}/`;
          this.subjects.push(el);
        }
      });

      this.subjects.forEach((el) => {
        el.full = `${el.code}-${el.description}`;
      });

      axios.get("/bccapi/aosfs").then((res) => {
        this.aosf = res.data;
      });

      axios.get("/bccapi/enrolls/" + this.student_id).then((ress) => {
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

<style></style>
