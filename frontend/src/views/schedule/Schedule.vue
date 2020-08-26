<template>
  <div>
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
      <el-row justify="end" :gutter="4">
        <el-radio-group
          size="small"
          v-model="radio"
          @change="searchAll"
          style="padding-top:6px; padding-right:4px;"
        >
          <el-radio-button label="by Instructor"></el-radio-button>
          <el-radio-button label="by Class"></el-radio-button>
          <el-radio-button label="all"></el-radio-button>
        </el-radio-group>
        <el-button @click="showAddDialog" size="small" type="success" icon="el-icon-plus"
          >Add Schedule</el-button
        >
      </el-row>
      <br />
      <br />
      <h6>Search Parameters</h6>
      <div v-show="radio == 'by Instructor'">
        <el-row :gutter="5">
          <el-col :md="6">
            <el-select
              filterable
              style="width: 100%;"
              size="small"
              v-model="instructor_pk"
              placeholder="select instructor"
            >
              <el-option value="">select instructor</el-option>
              <el-option
                v-for="(item, index) in instructors"
                :key="index"
                :label="`${item.last_name}` + `, ${item.first_name}`"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :md="6">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="ay_pk"
              placeholder="select Academic Year"
            >
              <el-option value="">select Academic Year</el-option>
              <el-option
                v-for="(item, index) in ays"
                :key="index"
                :label="item.ay"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :md="6">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="sem"
              placeholder="select sem"
            >
              <el-option value="">select sem</el-option>
              <el-option
                v-for="(item, index) in sems"
                :key="index"
                :label="`${item} ${item != 'summer' ? 'sem' : ''}`"
                :value="item"
              ></el-option>
            </el-select>
          </el-col>

          <el-col :md="6">
            <el-button
              style="width: 100%;"
              @click="searchbyInstructor(sem, ay_pk, instructor_pk)"
              :disabled="instructor_pk == '' || ay_pk == '' || sem == ''"
              size="small"
              type="primary"
              >Search
            </el-button>
          </el-col>
        </el-row>
      </div>
      <div v-show="radio == 'by Class'">
        <el-row :gutter="5">
          <el-col :md="8">
            <el-select
              filterable
              style="width: 100%;"
              size="small"
              v-model="course_pk"
              placeholder="select course"
            >
              <el-option value="">select course</el-option>
              <el-option
                v-for="(item, index) in courses"
                :key="index"
                :label="item.code"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="year_level_pk"
              placeholder="select year level"
            >
              <el-option value="">select year level</el-option>
              <el-option
                v-for="(item, index) in year_levels"
                :key="index"
                :label="`${item.code} year`"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="major_pk"
              placeholder="select major"
            >
              <el-option value="">select major</el-option>
              <el-option
                v-for="(item, index) in majors"
                :key="index"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row style="margin-top: 5px;" :gutter="5">
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="ay_pk"
              placeholder="select Academic Year"
            >
              <el-option value="">select Academic Year</el-option>
              <el-option
                v-for="(item, index) in ays"
                :key="index"
                :label="item.ay"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :md="8">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="sem"
              placeholder="select sem"
            >
              <el-option value="">select sem</el-option>
              <el-option
                v-for="(item, index) in sems"
                :key="index"
                :label="`${item} ${item != 'summer' ? 'sem' : ''}`"
                :value="item"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="4">
            <el-select
              style="width: 100%;"
              size="small"
              v-model="section"
              placeholder="sections"
            >
              <el-option value="">select sections</el-option>
              <el-option
                v-for="(item, index) in sections"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="4">
            <el-button
              style="width: 100%;"
              @click="search"
              :disabled="
                course_pk == '' ||
                  ay_pk == '' ||
                  course_pk == '' ||
                  sem == '' ||
                  section == '' ||
                  year_level_pk == '' ||
                  course_pk == ''
              "
              size="small"
              type="primary"
              >Search</el-button
            >
          </el-col>
        </el-row>
      </div>
    </el-card>

    <el-card>
      <el-row>
        <v-client-table :columns="columns" :data="instructor_loads_read">
          <a slot="action" slot-scope="props">
            <el-button
              type="success"
              @click="update(props.row.id)"
              size="small"
              circle
              icon="el-icon-edit"
            ></el-button
          ></a>
        </v-client-table>
        <el-col>
          <el-button
            v-show="radio == 'by Class'"
            :disable="instructor_loads_read.length == 0"
            @click="printClass(instructor_loads_read)"
          >
            print class schedule
          </el-button>
          <el-button
            :disable="instructor_loads_read.length == 0"
            v-show="radio == 'by Instructor'"
            @click="printByInstructor(instructor_loads_read)"
          >
            print instructor schedule
          </el-button>
        </el-col>
      </el-row>
    </el-card>
    <el-dialog
      title="Add Instructor"
      :visible.sync="dialogInstructor"
      width="40%"
      center
    >
      <el-form size="small" :ref="formInstructor" :model="formInstructor">
        <el-row>
          <el-col>
            <el-form-item label="Fist name">
              <el-input
                placeholder=" input first name"
                size="small"
                v-model="formInstructor.first_name"
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-form-item label="Middle name">
              <el-input
                placeholder=" input first name"
                size="small"
                v-model="formInstructor.middle_name"
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-form-item label="Last name">
              <el-input
                placeholder=" input first name"
                size="small"
                v-model="formInstructor.last_name"
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogInstructor = false">Cancel</el-button>
        <el-button type="primary" @click="saveInstructor()">Save</el-button>
      </span>
    </el-dialog>

    <el-dialog
      title="Add Instructor"
      :visible.sync="dialogRoom"
      width="40%"
      center
    >
      <el-form size="small" :ref="formRoom" :model="formRoom">
        <el-row>
          <el-col>
            <el-form-item label="Room name">
              <el-input
                placeholder=" input room name"
                size="small"
                v-model="formRoom.name"
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogRoom = false">Cancel</el-button>
        <el-button type="primary" @click="saveRoom()">Save</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="Add Instructor's Schedule"
      :visible.sync="dialog"
      width="40%"
      center
    >
      <el-form size="small" :ref="form" :model="form">
        <el-row :gutter="4">
          <el-col :span="23">
            <el-form-item label="Instructor">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select  instructor"
                v-model="form.instructor"
              >
                <el-option
                  v-for="(item, index) in instructors"
                  :label="`${item.last_name}` + `, ${item.first_name}`"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="1" style="padding-top:40px;">
            <el-button
              size="mini"
              @click="dialogInstructor = true"
              icon="el-icon-plus"
              circle
            ></el-button>
          </el-col>
        </el-row>
        <el-row :gutter="4">
          <el-col :span="12">
            <el-form-item label="Semester">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a semester"
                v-model="form.semister"
                @change="searchRooms"
              >
                <el-option
                  v-for="(item, index) in sems"
                  :label="`${item} ${item != 'summer' ? 'sem' : ''}`"
                  :value="item"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Academic Year">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a academic year"
                v-model="form.academic_year"
                @change="searchRooms"
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
        <el-row :gutter="4">
          <el-col :span="12">
            <el-form-item label="Course">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a course"
                v-model="form.course"
              >
                <el-option
                  v-for="(item, index) in courses"
                  :label="item.code"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="Major">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a major"
                v-model="form.major"
              >
                <el-option label="None" value=""> </el-option>
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
        </el-row>
        <el-row :gutter="4">
          <el-col :span="12">
            <el-form-item label="Year Level">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a year level"
                v-model="form.year_level"
              >
                <el-option
                  v-for="(item, index) in year_levels"
                  :label="item.code"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Section">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a subject"
                v-model="form.section"
              >
                <el-option
                  v-for="(item, index) in sections"
                  :label="item"
                  :value="item"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Subject">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a subject"
                v-model="form.subject"
              >
                <el-option
                  v-for="(item, index) in subjects"
                  :label="
                    `${item.code}` +
                      `-${item.description.replace('Lec/Lab', '')}`
                  "
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12" style="padding-top:40px;">
            <el-form-item>
              <el-checkbox v-model="form.is_lab">is Laboratory</el-checkbox>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="4">
          <el-col :span="12">
            <el-form-item label="Days">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a days"
                v-model="form.schedule_days"
                @change="
                  searchRooms();
                  filterTimeByDays();
                "
              >
                <el-option
                  v-for="(item, index) in days"
                  :label="item.day"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="Time">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a time"
                v-model="form.time"
                @change="searchRooms"
              >
                <el-option
                  v-for="(item, index) in filter_times"
                  :label="convertTime(item.time_start, item.duration_in_hour)"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="4">
          <el-col :span="23">
            <el-form-item label="Room">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a room"
                v-model="form.room"
                :disabled="form.semister == ''"
              >
                <el-option
                  v-for="(item, index) in rooms_filter"
                  :label="item.name"
                  :value="item.id"
                  :key="index"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="1" style="padding-top:40px;">
            <el-button
              @click="dialogRoom = true"
              size="mini"
              icon="el-icon-plus"
              circle
            ></el-button>
          </el-col>
        </el-row>
        <el-row
          ><el-col>
            <el-form-item label="Remarks">
              <el-input v-model="form.remarks"></el-input>
            </el-form-item> </el-col
        ></el-row>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialog = false">Cancel</el-button>
        <el-button
          v-show="form.id == ''"
          :disabled="
            form.year_level == '' ||
              form.course == '' ||
              form.semister == '' ||
              form.academic_year == '' ||
              form.time == '' ||
              form.schedule_days == '' ||
              form.room == '' ||
              form.instructor == '' ||
              form.subject == ''
          "
          type="primary"
          @click="save"
          >Save</el-button
        >
        <el-button
          v-show="form.id != ''"
          :disabled="
            form.year_level == '' ||
              form.course == '' ||
              form.semister == '' ||
              form.academic_year == '' ||
              form.time == '' ||
              form.schedule_days == '' ||
              form.room == '' ||
              form.instructor == '' ||
              form.subject == ''
          "
          type="primary"
          @click="updateSchedule"
          >Update</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
/* eslint-disable */
import moment from "moment";
import pdfMake from "pdfmake/build/pdfmake";
import pdfFonts from "pdfmake/build/vfs_fonts";
pdfMake.vfs = pdfFonts.pdfMake.vfs;
moment().format();
export default {
  data() {
    return {
      columns: [
        "instructor",
        "course_year_section",
        "academic_year",
        "semister",
        "subject",
        "schedule_days",
        "time",
        "room",
        "type",
        "action",
      ],
      radio: "all",
      dialog: false,
      dialogInstructor: false,
      dialogRoom: false,
      isLoading: true,
      fullPage: false,
      subject_pk: "",
      student_pk: "",
      instructor_pk: "",
      major_pk: "",
      sem: "",
      course_pk: "",
      year_level_pk: "",
      ay_pk: "",
      students: [],
      ids: [],
      isLoading: true,
      fullPage: false,
      subjects: [],
      dialog: false,
      section: "",
      sems: ["1st", "2nd", "summer"],
      sections: ["None", "A", "B", "C", "D", "E", "F"],
      ays: [],
      majors: [],
      year_levels: [],
      subjects: [],
      rooms: [],
      rooms_filter: [],
      times: [],
      days: [],
      instructors: [],
      instructor_loads: [],
      instructor_loads_read: [],
      courses: [],
      filter_times: [],
      tth_vacants: [],
      mwf_vacants: [],
      mw_vacants: [],
      merge_mw_mwf_vacants: [],

      form: {
        semister: "",
        academic_year: "",
        course: "",
        major: "",
        year_level: "",
        subject: "",
        time: "",
        schedule_days: "",
        room: "",
        instructor: "",
        is_lab: false,
        section: "",
        remarks: "",
        major_ids: "",
        majors: [],
      },
      formInstructor: {
        first_name: "",
        middle_name: "",
        last_name: "",
      },
      formRoom: {
        name: "",
      },
    };
  },
  methods: {
    update(id) {
      axios.get("/bccapi/instructorloads/" + id).then((res) => {
        this.form = res.data;
        this.dialog = true;
        this.searchRooms();
        this.filterTime();
      });
    },
    saveRoom() {
      axios.post("/bccapi/rooms/", this.formRoom).then((res) => {
        this.rooms.push(res.data);
        this.dialogRoom = false;
      });
    },
    saveInstructor() {
      axios.post("/bccapi/instructors/", this.formInstructor).then((res) => {
        this.instructors.push(res.data);
        this.dialogInstructor = false;
      });
    },

    convertTime(val, duration) {
      return (
        moment(val, "HH:mm:ss").format("LT") +
        " - " +
        moment(val, "HH:mm:ss")
          .add(duration, "hours")
          .format("LT")
      );
    },
    convertToNumeral(val) {
      switch (val) {
        case "1st":
          return "I";
          break;
        case "2nd":
          return "II";
          break;
        case "3rd":
          return "III";
          break;
        case "4th":
          return "IV";
          break;
        case "5th":
          return "V";
          break;
        default:
          return "NONE";
          break;
      }
    },
    printByInstructor(instructor_loads_read) {
      var docDefinition = {
        // a string or { width: number, height: number }
        pageSize: "A4",

        // by default we use portrait, you can change it to landscape if you wish
        pageOrientation: "landscape",

        // [left, top, right, bottom] or [horizontal, vertical] or just a number for equal margins
        pageMargins: [20, 20, 20, 20],
        content: [
          {
            columns: [
              {
                fontSize: 18,
                width: "*",
                text: [
                  {
                    text: `INSTRUCTOR\'S SCHEDULE  ${this.sem} SEMESTER A.Y ${
                      this.ays.filter((f) => f.id == this.ay_pk)[0].ay
                    }`,
                    bold: true,
                  },
                ],
              },
            ],
          },
          {
            columns: [
              {
                fontSize: 16,
                width: "*",
                text: [
                  {
                    text: `${
                      this.instructors.filter(
                        (f) => f.id == this.instructor_pk
                      )[0].last_name
                    }, ${
                      this.instructors.filter(
                        (f) => f.id == this.instructor_pk
                      )[0].first_name
                    }`,
                    bold: true,
                  },
                ],
              },
            ],
          },
          {
            style: "tableExample",
            table: {
              widths: [140, "*", 40, 120, 160],
              body: [
                [
                  {
                    text: "TIME",
                    bold: true,
                    style: "tableHeader",
                  },
                  {
                    text: "Subject",
                    bold: true,
                    style: "tableHeader",
                  },
                  {
                    text: "DAYS",
                    bold: true,
                  },
                  {
                    text: "ROOM",
                    bold: true,
                  },
                  {
                    text: "COURSE/YEAR",
                    bold: true,
                  },
                ],
              ],
            },
          },
          {
            columns: [
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                width: 200,
                text: "TTH vacants",
                bold: true,
              },
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                width: 200,
                text: "MWF/MW vacants",
                bold: true,
              },
            ],
          },

          {
            columns: [
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                fontSize: 10,
                width: 200,
                type: "square",
                ul: this.tth_vacants,
              },
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                fontSize: 10,
                width: 200,
                type: "square",
                ul: this.mwf_vacants,
              },
            ],
          },
        ],

        styles: {
          header: {
            fontSize: 18,
            bold: true,
            margin: [0, 0, 0, 10],
          },
          subheader: {
            fontSize: 16,
            bold: true,
            margin: [0, 10, 0, 5],
          },
          tableExample: {
            margin: [0, 10, 0, 30],
          },
          tableHeader: {
            bold: true,
            fontSize: 13,
            color: "black",
          },
        },
        defaultStyle: {
          // alignment: 'justify'
        },
      };
      instructor_loads_read.forEach((el) => {
        docDefinition.content[2].table.body.push([
          {
            text: el.time,
            fontSize: 14,
          },
          {
            text: el.subject,
            fontSize: 14,
          },
          {
            text: el.schedule_days,
            fontSize: 14,
          },
          {
            text: el.room,
            fontSize: 14,
          },
          {
            text: el.course_year,
            fontSize: 14,
          },
        ]);
      });
      pdfMake.createPdf(docDefinition).open();
    },

    printClass(instructor_loads_read) {
      let major =
        this.major_pk != ""
          ? this.majors.filter((f) => f.id == this.major_pk)[0].name
          : "NONE";
      let year_level = this.convertToNumeral(
        this.year_levels.filter((f) => f.id == this.year_level_pk)[0].code
      );
      var docDefinition = {
        // a string or { width: number, height: number }
        pageSize: "A4",

        // by default we use portrait, you can change it to landscape if you wish
        pageOrientation: "landscape",

        // [left, top, right, bottom] or [horizontal, vertical] or just a number for equal margins
        pageMargins: [20, 20, 20, 20],
        content: [
          {
            columns: [
              {
                fontSize: 18,
                width: "*",
                text: [
                  {
                    text: `CLASS SCHEDULE  ${this.sem} SEMESTER A.Y ${
                      this.ays.filter((f) => f.id == this.ay_pk)[0].ay
                    }`,
                    bold: true,
                  },
                ],
              },
            ],
          },
          {
            columns: [
              {
                fontSize: 16,
                width: "*",
                text: [
                  {
                    text: `${
                      this.courses.filter((f) => f.id == this.course_pk)[0].code
                    }${year_level}-${this.section}  MAJOR: ${major}`,
                    bold: true,
                  },
                ],
              },
            ],
          },
          {
            style: "tableExample",
            table: {
              widths: [140, "*", 40, 120, 160],
              body: [
                [
                  {
                    text: "TIME",
                    bold: true,
                    style: "tableHeader",
                  },
                  {
                    text: "Subject",
                    bold: true,
                    style: "tableHeader",
                  },
                  {
                    text: "DAYS",
                    bold: true,
                  },
                  {
                    text: "ROOM",
                    bold: true,
                  },
                  {
                    text: "INSTRUCTOR",
                    bold: true,
                  },
                ],
              ],
            },
          },
          {
            columns: [
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                width: 200,
                text: "TTH vacants",
                bold: true,
              },
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                width: 200,
                text: "MWF/MW vacants",
                bold: true,
              },
            ],
          },

          {
            columns: [
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                fontSize: 10,
                width: 200,
                type: "square",
                ul: this.tth_vacants,
              },
              {
                // to treat a paragraph as a bulleted list, set an array of items under the ul key
                fontSize: 10,
                width: 200,
                type: "square",
                ul: this.mwf_vacants,
              },
            ],
          },
        ],

        styles: {
          header: {
            fontSize: 18,
            bold: true,
            margin: [0, 0, 0, 10],
          },
          subheader: {
            fontSize: 16,
            bold: true,
            margin: [0, 10, 0, 5],
          },
          tableExample: {
            margin: [0, 10, 0, 30],
          },
          tableHeader: {
            bold: true,
            fontSize: 13,
            color: "black",
          },
        },
        defaultStyle: {
          // alignment: 'justify'
        },
      };
      instructor_loads_read.forEach((el) => {
        docDefinition.content[2].table.body.push([
          {
            text: el.time,
            fontSize: 14,
          },
          {
            text: el.subject,
            fontSize: 14,
          },
          {
            text: el.schedule_days,
            fontSize: 14,
          },
          {
            text: el.room,
            fontSize: 14,
          },
          {
            text: el.instructor,
            fontSize: 14,
          },
        ]);
      });
      pdfMake.createPdf(docDefinition).open();
    },
    //Filter  time by days
    filterTimeByDays() {
      if (this.form.time != "") {
        this.form.time = "";
      }
      this.filter_times = this.times.filter(
        (f) => f.days.id == this.form.schedule_days
      );
    },
    //Filter time but dont clear its form input
    filterTime() {
      this.filter_times = this.times.filter(
        (f) => f.days.id == this.form.schedule_days
      );
    },

    tranformToCourseYearSection(instructorsLoad) {
      return `${instructorsLoad.course.code}-${this.convertToNumeral(
        instructorsLoad.year_level.code
      )} ${instructorsLoad.section} ${
        instructorsLoad.major != null
          ? this.majors.filter((f) => f.id == instructorsLoad.major.id)[0].name
          : ""
      } ${instructorsLoad.remarks != null ? instructorsLoad.remarks : ""}`;
    },

    filterAndSortInstructorsLoad(filterInstructorLoad) {
      let sortInstructorLoad = [];
      let filter_tth = filterInstructorLoad
        .filter((f) => f.schedule_days == "TTH")
        .sort((a, b) => (a.startTime > b.startTime ? 1 : -1));

      let filter_mw = filterInstructorLoad
        .filter((f) => f.schedule_days == "MW")
        .sort((a, b) => (a.startTime > b.startTime ? 1 : -1));

      let filter_mwf = filterInstructorLoad
        .filter((f) => f.schedule_days == "MWF")
        .sort((a, b) => (a.startTime > b.startTime ? 1 : -1));

      let filter_other_day = filterInstructorLoad
        .filter(
          (f) =>
            f.schedule_days != "MWF" &&
            f.schedule_days != "MW" &&
            f.schedule_days != "TTH"
        )
        .sort((a, b) => (a.startTime > b.startTime ? 1 : -1));

      return sortInstructorLoad
        .concat(filter_mwf)
        .concat(filter_mw)
        .concat(filter_tth)
        .concat(filter_other_day);
    },

    getTTHVacants() {
      let filterTthTimes = this.times.filter(
        (t) =>
          t.days.day == "TTH" &&
          moment(t.time_start, "HH:mm:ss").format("LT") != "5:30 PM"
      );

      return filterTthTimes.map((el) => {
        let filterExist = this.instructor_loads_read.filter(
          (f) => f.startTimeId == el.id
        );
        if (filterExist.length == 0) {
          return el;
        }
      });
    },

    getMWFVacants(strDays) {
      let filterMwfTimes = this.times.filter(
        (t) =>
          t.days.day == strDays &&
          moment(t.time_start, "HH:mm:ss").format("LT") != "5:00 PM" &&
          moment(t.time_start, "HH:mm:ss").format("LT") != "6:00 PM"
      );

      return filterMwfTimes.map((el) => {
        let filterExist = this.instructor_loads_read.filter(
          (f) => f.startTimeId == el.id
        );
        if (filterExist.length == 0) {
          return el;
        }
      });
    },

    mergeMWAndMWFVacants(mwVacants, mwfVacants) {
      return mwVacants.map((e) => {
        let filterExist = mwfVacants.filter(
          (f) => f.time_start == e.time_start
        );
        if (filterExist.length > 0) {
          return e;
        }
      });
    },

    contcatSubjectAndDescription(subject) {
      return subject.code + " - " + subject.description.replace("Lec/Lab", "");
    },

    mapInstructorsLoadFromResponse(response) {
      return response.data.map((el) => {
        let type = el.is_lab ? "Laboratory" : "Lecture";
        let courseYearSection = this.tranformToCourseYearSection(el);

        return {
          instructor: `${el.instructor.last_name}, ${el.instructor.first_name}`,
          course_year_section: courseYearSection,
          academic_year: el.academic_year.ay,
          semister: el.semister,
          subject: this.contcatSubjectAndDescription(el.subject),
          schedule_days: el.schedule_days.day,
          time: this.convertTime(el.time.time_start, el.time.duration_in_hour),
          room: el.room.name,
          type: type,
          startTime: el.time.time_start,
          duration: el.time.duration_in_hour,
          startTimeId: el.time.id,
          dayId: el.schedule_days.id,
          course_year: courseYearSection,
        };
      });
    },

    async search() {
      let major = this.major_pk == "" ? "-1" : this.major_pk;
      // Actual api calls to get instructor's load
      let response = await axios.get(
        `/bccapi/IntructorLoadedSubjectByClassList/${this.sem}/${this.ay_pk}/${this.course_pk}/${major}/${this.section}/${this.year_level_pk}`
      );
      this.instructor_loads_read = [];
      // Map the response
      let filterInstructorLoad = this.mapInstructorsLoadFromResponse(response)
      // Sort Instructor's load
      let sortInstructorLoad = this.filterAndSortInstructorsLoad(
        filterInstructorLoad
      );

      let tthVacants = this.getTTHVacants();
      let mwfVacants = this.getMWFVacants("MWF");
      let mwVacants = this.getMWFVacants("MW");
      let mergeMWF = this.mergeMWAndMWFVacants(mwVacants, mwfVacants);

      this.tth_vacants = tthVacants.map((e) =>
        this.convertTime(e.time_start, e.duration_in_hour)
      );
      this.mwf_vacants = mergeMWF.map((e) =>
        this.convertTime(e.time_start, e.duration_in_hour)
      );
      this.instructor_loads_read = sortInstructorLoad;
    },

    searchAll() {
      axios.get("/bccapi/instructorloads-read").then((res) => {
        this.instructor_loads_read = [];
        let filterInstructorLoad = this.mapInstructorsLoadFromResponse(res)
        this.instructor_loads_read = filterInstructorLoad;
      });
    },
    async searchbyInstructor(sem, ay_pk, instructor_pk) {
      let response = await axios.get(
        `/bccapi/IntructorLoadedSubjectList/${this.sem}/${this.ay_pk}/${this.instructor_pk}`
      );
      this.instructor_loads_read = [];
      console.log(response.data);
      // Map the response
      let filterInstructorLoad = this.mapInstructorsLoadFromResponse(response)
      // Sort Instructor's load
      let sortInstructorLoad = this.filterAndSortInstructorsLoad(
        filterInstructorLoad
      );

      let tthVacants = this.getTTHVacants();
      let mwfVacants = this.getMWFVacants("MWF");
      let mwVacants = this.getMWFVacants("MW");
      let mergeMWF = this.mergeMWAndMWFVacants(mwVacants, mwfVacants);

      this.tth_vacants = tthVacants.map((e) =>
        this.convertTime(e.time_start, e.duration_in_hour)
      );
      this.mwf_vacants = mergeMWF.map((e) =>
        this.convertTime(e.time_start, e.duration_in_hour)
      );
      this.instructor_loads_read = sortInstructorLoad;
    },

    searchRooms() {
      let filterRooms = this.instructor_loads.filter(
        (load) =>
          load.semister == this.form.semister &&
          load.academic_year == this.form.academic_year &&
          load.time == this.form.time &&
          load.schedule_days == this.form.schedule_days
      );

      if (filterRooms.length > 0) {
        this.rooms_filter = this.rooms.filter((el) => {
          return filterRooms.some((f) => {
            return f.room != el.id;
          });
        });
      } else {
        this.rooms_filter = this.rooms;
      }
    },
    showAddDialog() {
      this.form = {
        id: "",
        semister: "",
        academic_year: "",
        course: "",
        major: "",
        year_level: "",
        subject: "",
        time: "",
        schedule_days: "",
        room: "",
        instructor: "",
        is_lab: false,
        section: "",
        remarks: "",
      };
      this.dialog = true;
    },
    refresh() {
      axios.get("/bccapi/instructorloads-read").then((response) => {
        this.instructor_loads_read = [];
        this.dialog = false;
        this.form = {
          id: "",
          semister: "",
          academic_year: "",
          course: "",
          major: "",
          year_level: "",
          subject: "",
          time: "",
          schedule_days: "",
          room: "",
          instructor: "",
          is_lab: false,
          section: "",
        };
        this.instructor_loads_read =  this.mapInstructorsLoadFromResponse(response)
      });
    },

    save() {
      axios
        .post("/bccapi/instructorloads/", this.form)
        .then((res) => {
          this.instructor_loads.push(res.data);
          this.refresh();
          this.$notify({
            title: "Success",
            message: "Save Successfully",
            type: "success",
          });
        })
        .catch((err) => {
          console.log(err);
          this.$notify.error({
            title: "Error",
            message: "Data Already Exists",
          });
        });
    },
    updateSchedule() {
      axios
        .put("/bccapi/instructorloads/" + this.form.id + "/", this.form)
        .then((res) => {
          this.instructor_loads.push(res.data);
          this.refresh();
          this.$notify({
            title: "Success",
            message: "Update Successfully",
            type: "success",
          });
        })
        .catch((err) => {
          console.log(err);
          this.$notify.error({
            title: "Error",
            message: "An Error occured",
          });
        });
    },
  },
  async created() {
    this.isLoading = true;
    let responseInstructorsLoad = await axios.get(
      "/bccapi/instructorloads-read"
    );
    this.instructor_loads_read = this.mapInstructorsLoadFromResponse(responseInstructorsLoad)
    this.isLoading = false;
    axios.get("/bccapi/ays").then((res) => {
      this.ays = res.data;
    });
    axios.get("/bccapi/rooms").then((res) => {
      this.rooms = res.data;
    });
    axios.get("/bccapi/times").then((res) => {
      this.times = res.data;
    });
    axios.get("/bccapi/days").then((res) => {
      this.days = res.data;
    });
    axios.get("/bccapi/majors").then((res) => {
      this.majors = res.data;
    });
    axios.get("/bccapi/subjects").then((res) => {
      this.subjects = res.data;
    });
    axios.get("/bccapi/yearlevels").then((res) => {
      this.year_levels = res.data;
    });
    axios.get("/bccapi/instructors").then((res) => {
      this.instructors = res.data;
    });
    axios.get("/bccapi/instructorloads").then((res) => {
      this.instructor_loads = res.data;
    });
    axios.get("/bccapi/courses").then((res) => {
      this.courses = res.data;
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
