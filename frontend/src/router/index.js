/* eslint-disable */

import Vue from "vue";
import Router from "vue-router";

// Containers
const DefaultContainer = () => import("@/containers/DefaultContainer");

// Views
const Dashboard = () => import("@/views/Dashboard");

// Users

const Login = () => import("@/views/pages/Login");
const Register = () => import("@/views/pages/Register");
const Curriculum = () => import("@/views/curriculum/Curriculum");
const Subject = () => import("@/views/subject/Subject");
const Schedule = () => import("@/views/schedule/Schedule");
const AddStudentAdmin = () => import("@/views/student/Add-student-admin");
const AddStudentUser = () => import("@/views/student/Add-student-user");
const StudentList = () => import("@/views/student/Student-List");
const EditStudent = () => import("@/views/student/Edit-Student");
const EnrollList = () => import("@/views/enroll/Student-Enroll");
const EnrollExportToExcel = () => import("@/views/enroll/Export-Enroll-Student");
const EnrollAddStudentId = () => import("@/views/enroll/Enroll-Add-Student-Id");
const EnrollListStudent = () => import("@/views/enroll/Enroll-List-Student");
const EnrollDetailsAdmin = () => import("@/views/enroll/Enroll-Details-Admin");
const EnrollDetailsStudent = () => import("@/views/enroll/Enroll-Details-Student");
const EnrollUser = () => import("@/views/enroll/Enroll-User");
const AddGrade = () => import("@/views/grade/Add-Grade");

Vue.use(Router);

export default new Router({
  mode: "history", // https://router.vuejs.org/api/#mode
  linkActiveClass: "open active",
  scrollBehavior: () => ({
    y: 0,
  }),
  routes: [{
      path: "/app/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/app/register",
      name: "Register",
      component: Register,
    },
    {
      path: "/",
      redirect: "/app/dashboard",
      name: "Home",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "/app/dashboard",
        name: "Dashboard",
        component: Dashboard,
        meta: {
          requiresAuth: true,
        },
      }, ],
    },
    {
      path: "/app/student",

      name: "Manage Student",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "add",
        name: "student-add",
        component: AddStudentAdmin,
        meta: {
          requiresAuth: true,
        },
      },
      {
        path: "user/add",
        name: "student-add-user",
        component: AddStudentUser,
        meta: {
          requiresAuth: true,
        },
      },
      {
        path: "list",
        name: "student-list",
        component: StudentList,
        meta: {
          requiresAuth: true,
        },
      },
      {
        path: "list/:id",
        name: "student-edit",
        component: EditStudent,
        meta: {
          requiresAuth: true,
        },
      },
     ],
    },
    {
      path: "/app/enroll",
      name: "Manage Enroll",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "list",
        name: "enroll-list",
        component: EnrollList,
        meta: {
          requiresAuth: true,
        },
        }, 
        {
          path: "list-student",
          name: "enroll-list-student",
          component: EnrollListStudent,
          meta: {
            requiresAuth: true,
          },
          },
        {
          path: "list/:id",
          name: "enroll-details",
          component: EnrollDetailsAdmin,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "student/:id",
          name: "enroll-student",
          component: EnrollUser,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "student/details/:id",
          name: "enroll-student-details",
          component: EnrollDetailsStudent,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "export",
          name: "enroll-export",
          component: EnrollExportToExcel,
          meta: {
            requiresAuth: true,
          },
        },
        {
          path: "check",
          name: "enroll-check-student_id",
          component: EnrollAddStudentId,
          meta: {
            requiresAuth: true,
          },
        },
        ],
    },
    {
      path: "/app/curriculum",

      name: "Manage Curriculum",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "list",
        name: "curriculum-list",
        component: Curriculum,
        meta: {
          requiresAuth: true,
        },
      }, ],
    },
    {
      path: "/app/grade",

      name: "Manage Grade",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "add",
        name: "grade-add",
        component: AddGrade,
        meta: {
          requiresAuth: true,
        },
      }, ],
    },
    {
      path: "/app/subject",

      name: "Manage Subject",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "list",
        name: "subject-list",
        component: Subject,
        meta: {
          requiresAuth: true,
        },
      }, ],
    },
    {
      path: "/app/schedule",

      name: "Manage Schedule",
      component: DefaultContainer,
      meta: {
        requiresAuth: true,
      },
      children: [{
        path: "list",
        name: "schedule-list",
        component: Schedule,
        meta: {
          requiresAuth: true,
        },
      }, ],
    },
  ],
});