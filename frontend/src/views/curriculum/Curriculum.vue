<template>
  <div style="padding: 20px 20px;">
    <el-card>
      <el-row>
        <el-col :md="6">
          <el-button type="primary" size="small" @click="showDialog">add Curriculum</el-button>
        </el-col>
      </el-row>
      <hr />

      <v-client-table :columns="columns" :data="datas">
        <el-button
          type="success"
          slot="action"
          @click="showedit(props.row.uri)"
          slot-scope="props"
          size="small"
          icon="el-icon-edit"
          circle
        ></el-button>
      </v-client-table>
    </el-card>

    <el-dialog title="Add Curriculum" :visible.sync="dialog" width="60%" center>
      <el-form :ref="form" :model="form" size="small">
        <el-row :gutter="5">
          <el-col :md="12">
            <el-form-item label="course">
              <el-select style="width: 100%;" v-model="form.course" placeholder="Course">
                <el-option value>Course</el-option>
                <el-option
                  v-for="(item, index) in courses"
                  :label="item.code"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="major">
              <el-select style="width: 100%;" v-model="form.major" placeholder="Major">
                <el-option value>Major</el-option>
                <el-option
                  v-for="(item, index) in majors"
                  :label="item.name"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="year level">
              <el-select style="width: 100%;" v-model="form.year_level" placeholder="Year">
                <el-option value>Year</el-option>
                <el-option
                  v-for="(item, index) in yearlevels"
                  :label="item.description"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="semister">
              <el-select style="width: 100%;" v-model="form.semister" placeholder="Semister">
                <el-option value>Semister</el-option>
                <el-option v-for="(item, index) in sems" :label="item" :value="item" :key="index"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <hr />
        <el-row :gutter="5">
          <el-col :md="20">
            <el-select
              filterable
              size="small"
              style="width: 100%;"
              placeholder="subject"
              v-model="subject_id"
            >
              <el-option value>Subject</el-option>
              <el-option
                v-for="(item, index) in subjects"
                :value="item.id"
                :label="item.full"
                :key="index"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="4">
            <el-button style="width: 100%;" @click="addSub" type="success" size="small">Add</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-table :data="subjects_selected" style="width: 100%">
            <el-table-column prop="code" label="Code" width="100"></el-table-column>
            <el-table-column prop="description" label="Descriptive Title"></el-table-column>
            <el-table-column prop="unit" label="Unit"></el-table-column>

            <el-table-column fixed="right" label="action" width="120">
              <template slot-scope="scope">
                <el-button
                  @click.native.prevent="deleteRow(scope.$index, subjects_selected,form.subjects)"
                  type="danger"
                  size="small"
                >Remove</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-row>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialog = false">Cancel</el-button>
        <el-button
          :disabled="form.course==''|| form.year_level =='' || form.semister == '' || form.subjects.length ==0"
          type="primary"
          @click="save"
        >Save</el-button>
      </span>
    </el-dialog>

    <el-dialog title="Edit Curriculum" :visible.sync="dialogedit" width="60%" center>
      <el-form :ref="editform" :model="editform" size="small">
        <el-row :gutter="5">
          <el-col :md="12">
            <el-form-item label="course">
              <el-select style="width: 100%;" v-model="editform.course" placeholder="Course">
                <el-option value>Course</el-option>
                <el-option
                  v-for="(item, index) in courses"
                  :label="item.code"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="major">
              <el-select style="width: 100%;" v-model="editform.major" placeholder="Major">
                <el-option value>Major</el-option>
                <el-option
                  v-for="(item, index) in majors"
                  :label="item.name"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="year level">
              <el-select style="width: 100%;" v-model="editform.year_level" placeholder="Year">
                <el-option value>Year</el-option>
                <el-option
                  v-for="(item, index) in yearlevels"
                  :label="item.description"
                  :value="item.id"
                  :key="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :md="12">
            <el-form-item label="semister">
              <el-select style="width: 100%;" v-model="editform.semister" placeholder="Semister">
                <el-option value>Semister</el-option>
                <el-option v-for="(item, index) in sems" :label="item" :value="item" :key="index"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <hr />
        <el-row :gutter="5">
          <el-col :md="20">
            <el-select
              filterable
              size="small"
              style="width: 100%;"
              placeholder="subject"
              v-model="subject_id"
            >
              <el-option value>Subject</el-option>
              <el-option
                v-for="(item, index) in subjects"
                :value="item.id"
                :label="item.full"
                :key="index"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :md="4">
            <el-button style="width: 100%;" @click="addSubedit" type="success" size="small">Add</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-table :data="subjects_selectededit" style="width: 100%">
            <el-table-column prop="code" label="Code" width="100"></el-table-column>
            <el-table-column prop="description" label="Descriptive Title"></el-table-column>
            <el-table-column prop="unit" label="Unit"></el-table-column>

            <el-table-column fixed="right" label="action" width="120">
              <template slot-scope="scope">
                <el-button
                  @click.native.prevent="deleteRowedit(scope.$index, subjects_selectededit,editform.subjects)"
                  type="danger"
                  size="small"
                >Remove</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-row>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogedit = false">Cancel</el-button>
        <el-button
          :disabled="editform.course==''|| editform.year_level =='' || editform.semister == '' || editform.subjects.length ==0"
          type="primary"
          @click="update"
        >Update</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  data() {
    return {
      columns: ["full", "course", "major", "semister", "year_level", "action"],
      datas: [],
      dialog: false,
      dialogedit: false,
      sems: ["1st", "2nd", "summer"],
      statuses: ["passed", "failed", "no grade", "inc"],
      curriculums: [],
      subjects: [],
      yearlevels: [],
      majors: [],
      courses: [],
      sems: ["1st", "2nd", "summer"],
      subject_id: "",
      subjects_selected: [],
      form: {
        year_level: "",
        semister: "",
        course: "",
        slug: "",
        major: "",
        subjects: []
      },
      editform: {
        year_level: "",
        semister: "",
        course: "",
        slug: "",
        major: "",
        subjects: []
      },
      subjects_selectededit: []
    };
  },
  methods: {
    showedit(uri) {
      axios.get(uri).then(res => {
        this.dialogedit = true;
        this.editform = res.data;
        console.log(res.data);
        this.subjects_selectededit = [];
        this.editform.subjects.forEach(el => {
          subject = this.subjects.find(e => e.id == el);
          this.subjects_selectededit.push(subject);
        });
      });
    },
    deleteRow(index, rows, datas) {
      rows.splice(index, 1);
      datas.splice(index, 1);
    },
    deleteRowedit(index, rows, datas) {
      rows.splice(index, 1);
      datas.splice(index, 1);
    },
    addSub() {
      let subject = this.subjects.find(el => el.id == this.subject_id);

      if (this.form.subjects.find(e => e == this.subject_id) == null) {
        this.form.subjects.push(this.subject_id);
        this.subjects_selected.push(subject);
      }
    },
    addSubedit() {
      let subject = this.subjects.find(el => el.id == this.subject_id);

      if (this.editform.subjects.find(e => e == this.subject_id) == null) {
        this.editform.subjects.push(this.subject_id);
        this.subjects_selectededit.push(subject);
      }
    },
    showDialog() {
      this.dialog = true;
    },
    update() {
      axios
        .put("/bccapi/curriculums/" + this.editform.id + "/", this.editform)
        .then(res => {
          console.log(res.data);
          this.dialogedit = false;
        });
    },
    save() {
      let major = this.form.major != "" ? this.form.major : "";
      this.form.slug = `${this.form.course}${this.form.year_level}${this.form.semister}${major}`;
      if (this.datas.find(el => el.slug == this.form.slug) == null) {
        axios.post("/bccapi/curriculums/", this.form).then(res => {
          console.log(res.data);
        });
        console.log("not exist");
        console.log(this.form.slug);
      } else {
        console.log("already exist");
      }
    }
  },
  created() {
    axios.get("/bccapi/subjects").then(res => {
      this.subjects = res.data;
      console.log(res.data);
      this.subjects.forEach(el => {
        el.full = `${el.code}-${el.description}`;
      });
    });
    axios.get("/bccapi/courses").then(res => {
      this.courses = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/yearlevels").then(res => {
      this.yearlevels = res.data;
      console.log(res.data);
    });
    axios.get("/bccapi/majors").then(res => {
      this.majors = res.data;
      console.log(res.data);
    });

    axios.get("/bccapi/curriculums").then(res => {
      this.datas = res.data;
      console.log(res.data);
      this.datas.forEach(el => {
        let course = this.courses.find(e => e.id == el.course);
        let year = this.yearlevels.find(e => e.id == el.year_level);
        let major = this.majors.find(e => e.id == el.major);
        el.major = major != null ? major.name : "";
        el.year_level = year.description;
        el.course = course.code;
        el.uri = `/bccapi/curriculums/${el.id}/`;
        el.full = `${year.description} ${course.code} ${
          major != null ? major.name : ""
        } ${el.semister}`;
      });
    });
  }
};
</script>

<style>
.el-form-item--small .el-form-item__content,
.el-form-item--small .el-form-item__label {
  line-height: 0px;
}
</style>