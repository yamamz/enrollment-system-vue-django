<template>
  <div>
    <el-form ref="form" :rules="rules" :model="form" size="small" label-position="top">
      <el-card>
        <el-row>
          <h5>Personal Information</h5>
          <hr />
        </el-row>
        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="Course" prop="course">
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
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Major" prop="major">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a major"
                v-model="form.major"
              >
                <el-option
                  v-for="(item, index) in majors"
                  :label="item.name"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Student Id" prop="student_id">
              <el-input placeholder="student id" v-model="form.student_id"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Lrn Number" prop="lrn_num">
              <el-input placeholder="lrn number" v-model="form.lrn_num"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="First Name" prop="first_name">
              <el-input placeholder="first name" v-model="form.first_name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Middle Name" prop="middle_name">
              <el-input placeholder="middle name" v-model="form.middle_name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Last Name" prop="last_name">
              <el-input placeholder="last name" v-model="form.last_name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Extension Name">
              <el-input placeholder="ext. name e.g JR/SR" v-model="form.ext_name"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="Provice" prop="province">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a province"
                v-model="provinceCode"
                @change="onChangeProvince"
              >
                <el-option
                  v-for="(item, index) in provinces"
                  :label="item.provDesc"
                  :value="item.provCode"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Municipality" prop="city">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a municipality"
                v-model="municipalityCode"
                @change="onChangeMunicipality"
              >
                <el-option
                  v-for="(item, index) in munipalityFilter"
                  :label="item.citymunDesc"
                  :value="item.citymunCode"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Barangay" prop="brgy">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a barangay"
                v-model="form.brgy"
              >
                <el-option
                  v-for="(item, index) in brgyFilter"
                  :label="item.brgyDesc"
                  :value="item.brgyDesc"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Street" prop="street">
              <el-input placeholder="e.g Purok no. or Name of Street" v-model="form.street"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="Postal Code" prop="zip_code">
              <el-input placeholder="postal code" v-model="form.zip_code"></el-input>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Email Address" prop="email_add">
              <el-input placeholder="email" v-model="form.email_add"></el-input>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Mobile Number" prop="mobile_no">
              <el-input placeholder="mobile no." v-model="form.mobile_no"></el-input>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Nationality" prop="nationality">
              <el-input placeholder="nationality" v-model="form.nationality"></el-input>
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="Birth Date" prop="birth_date">
              <el-date-picker
                style="width: 100%;"
                v-model="form.birth_date"
                type="date"
                placeholder="Pick a date"
              ></el-date-picker>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Place of birth" prop="place_of_birth">
              <el-input placeholder="place of bith" v-model="form.place_of_birth"></el-input>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Gender" prop="gender">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a gender"
                v-model="form.gender"
              >
                <el-option
                  v-for="(item, index) in genders"
                  :label="item"
                  :value="item"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Civil Status" prop="civil_status">
              <el-select
                filterable
                style="width: 100%;"
                placeholder="select a civil status"
                v-model="form.civil_status"
              >
                <el-option
                  v-for="(item, index) in civil_statuses"
                  :label="item"
                  :value="item"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <h5>Parents/Guardians Information</h5>
          <hr />
        </el-row>

        <el-row :gutter="8">
          <el-col :md="6">
            <el-form-item label="Parent/Guardian Fullname" prop="guardian">
              <el-input placeholder="Fullname" v-model="form.guardian"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Relationship" prop="relationship">
              <el-input placeholder="Relationship" v-model="form.relationship"></el-input>
            </el-form-item>
          </el-col>

          <el-col :md="6">
            <el-form-item label="Occupation" prop="occupation">
              <el-input placeholder="Occupation" v-model="form.occupation"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="Contact" prop="guardian_contact">
              <el-input placeholder="Contact" v-model="form.guardian_contact"></el-input>
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="8">
          <el-col :md="12">
            <el-form-item label="Guardian Address" prop="guardian_address">
              <el-input placeholder="Guardian Address" v-model="form.guardian_address"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="Religion" prop="religion">
              <el-input placeholder="Religion" v-model="form.religion"></el-input>
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="8">
          <el-col :md="18">
            <el-form-item label="Primary" prop="primary">
              <el-input placeholder="primary" v-model="form.primary"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="year completed" prop="primary_completed">
              <el-input placeholder="completed" v-model="form.primary_completed"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="8">
          <el-col :md="18">
            <el-form-item label="Elementary" prop="elementary">
              <el-input placeholder="elementary" v-model="form.elementary"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="year completed" prop="elementary_completed">
              <el-input placeholder="completed" v-model="form.elementary_completed"></el-input>
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="8">
          <el-col :md="18">
            <el-form-item label="Highschool" prop="highschool">
              <el-input placeholder="highschool" v-model="form.highschool"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="year completed" prop="highschool_completed">
              <el-input placeholder="completed" v-model="form.highschool_completed"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="8">
          <el-col :md="18">
            <el-form-item label="degree completed">
              <el-input placeholder="degree completed" v-model="form.degree_completed"></el-input>
            </el-form-item>
          </el-col>
          <el-col :md="6">
            <el-form-item label="year completed">
              <el-input placeholder="year completed" v-model="form.degree_year_attended"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <br />
        <el-alert
          v-if="!studentIdIsValid && form.student_id != ''"
          title="Student Id is not associated with your name"
          type="error"
        ></el-alert>
        <br />
        <el-button type="primary" plain :loading="isLoading" @click="save('form')">Save</el-button>
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

export default {
  data() {
    return {
      isLoading: false,
      genders: ["Male", "Female"],
      civil_statuses: ["Single", "Married", "Widow"],
      majors: [],
      courses: [],
      provinceKey: "",
      municipalKey: "",
      studentIdIsValid: true,
      provinces: [],
      municipalities: [],
      brgys: [],
      munipalityFilter: [],
      brgyFilter: [],

      provinceCode: null,
      municipalityCode: null,

      form: {
        student_id: "",
        first_name: "",
        middle_name: "",
        ext_name: "",
        gender: "",
        last_name: "",
        birth_date: "",
        address: "",
        brgy: "",
        street: "",
        city: "",
        province: "",
        place_of_birth: "",
        mobile_no: "",
        guardian: "",
        relationship: "",
        guardian_address: "",
        guardian_contact: "",
        occupation: "",
        religion: "",
        zip_code: "",
        course: "",
        major: "",
        primary: "",
        elementary: "",
        highschool: "",
        degree_completed: "",
        degree_year_attended: "",
        name_of_school: "",
        primary_completed: "",
        elementary_completed: "",
        highschool_completed: "",
        civil_status: "",
        nationality: "",
        email_add: "",
        lrn_num: ""
      },
      rules: {
        region: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        student_id: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        first_name: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        middle_name: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        ext_name: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        gender: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        last_name: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        birth_date: [
          { required: true, message: "Field is required", trigger: "change" }
        ],

        brgy: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        street: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        city: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        province: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        place_of_birth: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        mobile_no: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        guardian: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        relationship: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        guardian_address: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        guardian_contact: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        occupation: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        religion: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        zip_code: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        course: [
          { required: true, message: "Field is required", trigger: "change" }
        ],

        primary: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        elementary: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        highschool: [
          { required: true, message: "Field is required", trigger: "change" }
        ],

        primary_completed: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        elementary_completed: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        highschool_completed: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        civil_status: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        nationality: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        email_add: [
          { required: true, message: "Field is required", trigger: "change" }
        ],
        lrn_num: [
          { required: true, message: "Field is required", trigger: "change" }
        ]
      }
    };
  },
  methods: {
    async save(form) {
      let isStudentIdValidated = false;
      try {
        let studentResponse = await axios.get(
          "/bccapi/getIdAndFullname/" + this.form.student_id
        );
        console.log(studentResponse);
        isStudentIdValidated =
          studentResponse.data.length > 0 &&
          studentResponse.data[0].last_name != "" &&
          studentResponse.data[0].first_name != ""
            ? `${studentResponse.data[0].first_name
                .toUpperCase()
                .trim()} ${studentResponse.data[0].last_name
                .toUpperCase()
                .trim()}` ==
              `${this.form.first_name
                .toUpperCase()
                .trim()} ${this.form.last_name.toUpperCase().trim()}`
            : false;
        console.log(isStudentIdValidated);
        if (isStudentIdValidated) {
          this.studentIdIsValid = true;
        } else {
          this.studentIdIsValid = false;
        }
      } catch (e) {
        console.log(e);
      }

      this.$refs[form].validate(valid => {
        if (valid && isStudentIdValidated) {
          let birthDate = new Date(this.form.birth_date);

          let datestr = `${birthDate.getUTCMonth() +
            1}-${birthDate.getUTCDate()}-${birthDate.getFullYear()}`;
          this.form.birth_date = datestr;
          this.isLoading = true;

          axios
            .post("/bccapi/students/", this.form)
            .then(res => {
              this.isLoading = false;
              this.form = {
                student_id: "",
                first_name: "",
                middle_name: "",
                ext_name: "",
                gender: "",
                last_name: "",
                birth_date: "",
                address: "",
                brgy: "",
                street: "",
                city: "",
                province: "",
                place_of_birth: "",
                mobile_no: "",
                guardian: "",
                relationship: "",
                guardian_address: "",
                guardian_contact: "",
                occupation: "",
                religion: "",
                zip_code: "",
                course: "",
                major: "",
                primary: "",
                elementary: "",
                highschool: "",
                degree_completed: "",
                degree_year_attended: "",
                name_of_school: "",
                primary_completed: "",
                elementary_completed: "",
                highschool_completed: "",
                civil_status: "",
                nationality: "",
                email_add: "",
                lrn_num: ""
              };
                this.$router.push({ name: "student-list" });
            })
            .catch(e => {
               this.$notify({
            title: "Oops...",
            message: "Something went wrong!",
            type: "error",
          });
            });
        } else {
          return false;
        }
      });
    },
    onChangeProvince() {
      this.form.city = "";
      this.form.brgy = "";
      this.municipalityCode = "";
      this.form.province = this.provinces.find(
        el => el.provCode == this.provinceCode
      ).provDesc;
      this.munipalityFilter = this.municipalities.filter(
        el => el.provCode == this.provinceCode
      );
    },
    onChangeMunicipality() {
      this.form.brgy = "";
      this.form.city = this.municipalities.find(
        el => el.citymunCode == this.municipalityCode
      ).citymunDesc;

      this.brgyFilter = this.brgys.filter(
        el => el.citymunCode == this.municipalityCode
      );
      console.log(this.brgyFilter);
    },
    deleteRow(index, rows) {
      rows.splice(index, 1);
    }
  },
  created() {
      axios.get('/media/xls/adresses.json').then(res => {
          this.provinces = res.data.provinces;
          this.municipalities = res.data.municipalities;
          this.brgys = res.data.brgys;
      });
    axios.get("/bccapi/majors").then(res => {
      this.majors = res.data;
    });
    axios.get("/bccapi/courses").then(res => {
      this.courses = res.data;
    });
  }
};
</script>

<style>
</style>
