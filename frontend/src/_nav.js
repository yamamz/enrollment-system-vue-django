/* eslint-disable */
export default {
  items: [{
      name: "Dashboard",
      url: "/",
      icon: "icon-speedometer",
      isAdmin:false,
      // badge: {
      //   variant: 'primary',
      //   text: 'NEW'
      // }
    },
    {
      title: true,
      name: "Main",
    },
    {
      name: "Curriculum",
      url: "/curriculum",
      icon: "icon-note",
      isAdmin:true,
      children: [{
        name: "curriculum list",
        url: "/app/curriculum/list",
        icon: "icon-list",
      }, ],
    },
    // {
    //   name: "Student",
    //   url: "/students",
    //   icon: "icon-people",
    //   isAdmin:true,
    //   children: [{
    //     name: "student add",
    //     url: "/app/student/add",
    //     icon: "icon-user-follow",
    //   }, 
    //   {
    //     name: "student list",
    //     url: "/app/student/list",
    //     icon: "icon-list",
    //   }, 
    // ],
    // },
    // {

    //   name: "Manage Enroll",
    //   url: "/enrolls",
    //   icon: "icon-graduation",
    //   isAdmin:true,
    //   children: [{
    //     name: "enroll list",
    //     url: "/app/enroll/list",
    //     icon: "icon-user-follow",
    //   }, 
    //   {
    //     name: "enroll export",
    //     url: "/app/enroll/export",
    //     icon: "icon-share-alt",
    //   },
    // ],
    // },
    {
      name: "Subject",
      url: "/subjects",
      icon: "icon-book-open",
      isAdmin:true,
      children: [{
        name: "subject list",
        url: "/app/subject/list",
        icon: "icon-list",
      }, ],
    },
    {
      name: "Schedule",
      url: "/schedules",
      icon: "icon-calendar",
      isAdmin:true,
      children: [{
        name: "schedule list",
        url: "/app/schedule/list",
        icon: "icon-list",
      }, ],
    },
    // {
    //   name: "Manage Grade",
    //   url: "/schedules",
    //   icon: "icon-docs",
    //   isAdmin:true,
    //   children: [{
    //     name: "Add Grade",
    //     url: "/app/grade/add",
    //     icon: "icon-listicon-note",
    //   }, ],
    // },
    // {
    //   name: "Enroll as Student",
    //   url: "/schedules",
    //   icon: "icon-people",
    //   isAdmin:false,
    //   children: [{
    //     name: "Enroll as new",
    //     url: "/app/student/user/add",
    //     icon: "icon-note",
    //   },
    //   {
    //     name: "Enroll as old",
    //     url: "/app/enroll/check",
    //     icon: "icon-note",
    //   },
    //   {
    //     name: "My enrollment",
    //     url: "/app/enroll/list-student",
    //     icon: "icon-list",
    //   },
    //  ],
    // },
    {
      divider: true,
    },
    {
      title: true,
      name: "Extra",
    },
    {
      name: "Settings",
      url: "/Settings",
      icon: "icon-settings",
      isAdmin:false,
      children: [{
          name: "Login",
          url: "/app/login",
          icon: "icon-login",
        },
        {
          name: "Register",
          url: "/app/register",
          icon: "icon-user-follow",
        },
      ],
    },
  ],
};