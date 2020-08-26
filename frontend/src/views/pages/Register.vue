<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card no-body class="mx-4">
            <b-card-body class="p-4">
              <b-form>
                <h1>Register</h1>
                <p class="text-muted">Create your account</p>
                <b-input-group class="mb-3">
                  <b-input-group-prepend>
                    <b-input-group-text>
                      <i class="icon-user"></i>
                    </b-input-group-text>
                  </b-input-group-prepend>
                  <b-form-input
                    type="text"
                    class="form-control"
                    v-model="$v.username.$model"
                    placeholder="Username"
                    autocomplete="username"
                    :class="status($v.username)"
                  />
                </b-input-group>

                <b-input-group class="mb-3">
                  <b-input-group-prepend>
                    <b-input-group-text>
                      <i class="icon-lock"></i>
                    </b-input-group-text>
                  </b-input-group-prepend>
                  <b-form-input
                    v-model="$v.password.$model"
                    type="password"
                    class="form-control"
                    placeholder="Password"
                    autocomplete="new-password"
                    :class="status($v.password)"
                  />
                </b-input-group>

                <b-input-group class="mb-4">
                  <b-input-group-prepend>
                    <b-input-group-text>
                      <i class="icon-lock"></i>
                    </b-input-group-text>
                  </b-input-group-prepend>
                  <b-form-input
                    v-model="$v.repeatPassword.$model"
                    type="password"
                    class="form-control"
                    placeholder="Repeat password"
                    autocomplete="new-password"
                    :class="status($v.repeatPassword)"
                  />
                </b-input-group>

                <b-button @click="register()" variant="primary" :disable="!$v.password.$invalid && !$v.username.$invalid" block
                  >Create Account</b-button
                >
              </b-form>
            </b-card-body>
            <b-card-footer class="p-4">
              <div>
                <a href="https://github/yamamz">Raymundo T. Melecio</a>
                <span class="ml-1"
                  >Copyrigth &copy; 2019. all rights Reserved</span
                >
              </div>
            </b-card-footer>
          </b-card>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

import { required, sameAs, minLength } from "vuelidate/lib/validators";

export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      repeatPassword: "",
    };
  },
  validations: {
    username: {
      required,
      minLength: minLength(8),
    },
    password: {
      required,
      minLength: minLength(8),
    },
    repeatPassword: {
      sameAsPassword: sameAs("password"),
    },
  },
  methods: {
    register() {
      if (!this.$v.password.$invalid && !this.$v.username.$invalid && !this.$v.repeatPassword.$invalid ) {
        axios
          .post("/bccapi/createuser/", {
            username: this.username,
            password: this.password,
          })
          .then((res) => {
            this.$notify({
              title: "Success",
              message: "Register Successfully you can now login",
              type: "success",
            });
            this.$router.push({ name: "Login" });
          });
      }
    },
    status(validation) {
      return {
        error: validation.$error,
        dirty: validation.$dirty,
      };
    },
  },
};
</script>
<style>
.dirty {
  border-color: #5a5;
  background: #efe;
}

.dirty:focus {
  outline-color: #8e8;
}

.error {
  border-color: red;
  background: #fdd;
}

.error:focus {
  outline-color: #f99;
}
</style>
