<template>
  <div>
    <form
      id="form_upload111"
      data-href="{%url 'uploadSubjectsAPI'%}"
      method="POST"
      enctype="multipart/form-data"
    >
      <div class="form-group row">
        <div class="col-md-12"></div>
      </div>
    </form>
    <div class="card">
      <div class="card-header info-color">
        <el-button @click="add" size="small" type="primary">Add Subject</el-button>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <v-client-table :columns="columns" :data="subjects">
            <a slot="action" slot-scope="props">
              <el-button
                type="success"
                @click="update(props.row)"
                size="small"
                circle
                icon="el-icon-edit"
              ></el-button>
            </a>
          </v-client-table>
        </div>
      </div>
    </div>

    <el-dialog title="Add Subject" :visible.sync="dialog" width="40%" center>
      <el-form size="small" :ref="form" :model="form">
        <el-form-item label="Code">
          <el-input placeholder="code" v-model="form.code"></el-input>
        </el-form-item>
        <el-form-item label="Description">
          <el-input placeholder="description" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item label="Unit">
          <el-input placeholder="unit" type="number" v-model="form.unit"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialog = false">Cancel</el-button>
        <el-button
          :disabled="form.code==''|| form.description =='' || form.unit == ''"
          type="primary"
          @click="save"
        >Save</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      columns: ["code", "description", "unit", "action"],
      students: [],
      ids: [],
      isLoading: true,
      fullPage: false,
      subjects: [],
      dialog: false,

      form: {
        code: "",
        description: "",
        unit: ""
      }
    };
  },
  methods: {
    add() {
      this.form = {
        code: "",
        description: "",
        unit: ""
      };
      this.dialog = true;
    },
    update(subject) {
      this.form = subject;
      this.dialog = true;
    },
    save() {
      if (this.form.id == "") {
        axios
          .post("/bccapi/subjects/", this.form)
          .then(res => {
            console.log(res.data);
            this.dialog = false;
            //if(res.data.failed == true)
            this.subjects.push(res.data);
          })
          .catch(err => {
            this.$notify.error({
              title: "Error",
              message: "Data Already Exists"
            });
          });
      } else {
        axios
          .put("/bccapi/subjects/" + this.form.id + "/", this.form)
          .then(res => {
            console.log(res.data);
            //if(res.data.failed == true)
            //this.subjects.push(res.data)
            this.dialog = false;
            axios.get("subjects").then(res => {
              this.subjects = res.data;
            });
          })
          .catch(err => {
            this.$notify.error({
              title: "Error",
              message: "Error"
            });
          });
      }
    }
  },
  created() {
    axios.get("/bccapi/subjects").then(res => {
      this.subjects = res.data;
    });
  }
};
</script>
<style>
</style>
