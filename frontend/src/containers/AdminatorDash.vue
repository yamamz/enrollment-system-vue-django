<template>
  <div>
    <!-- #Left Sidebar ==================== -->
    <div class="sidebar">
      <div class="sidebar-inner">
        <!-- ### $Sidebar Header ### -->
        <div class="sidebar-logo">
          <div class="peers ai-c fxw-nw">
            <div class="peer peer-greed">
              <a class="sidebar-link td-n" href="/">
                <div class="peers ai-c fxw-nw">
                  <div class="peer">
                    <div class="logo">
                      <img
                        src="{%static 'student_profile/assetsadmin/static/images/logo.png'%}"
                        alt=""
                      />
                    </div>
                  </div>
                  <div class="peer peer-greed">
                    <h5 class="lh-1 mB-0 logo-text">BCC</h5>
                  </div>
                </div>
              </a>
            </div>
            <div class="peer">
              <div class="mobile-toggle sidebar-toggle">
                <a href="" class="td-n">
                  <i class="ti-arrow-circle-left"></i>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- ### $Sidebar Menu ### -->
        <ul class="sidebar-menu scrollable pos-r">
          <li class="nav-item mT-30 actived">
            <a class="sidebar-link" href="/">
              <span class="icon-holder">
                <i class="c-blue-500 ti-home"></i>
              </span>
              <span class="title">Dashboard</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="sidebar-link" href="{%url 'allStudentEnroll'%}">
              <span class="icon-holder">
                <i class="c-deep-orange-500 ti-calendar"></i>
              </span>
              <span class="title">View Enrollees</span>
            </a>
          </li>

          <li class="nav-item">
            <a class="sidebar-link" href="{%url 'addSubject'%}">
              <span class="icon-holder">
                <i class="c-deep-purple-500 ti-agenda"></i>
              </span>
              <span class="title">Manage Subjects</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="sidebar-link" href="{%url 'addCuriculum'%}">
              <span class="icon-holder">
                <i class="c-indigo-500 ti-bar-chart"></i>
              </span>
              <span class="title">Curriculums</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="sidebar-link" href="{%url 'allStudent'%}">
              <span class="icon-holder">
                <i class="c-light-blue-500 ti-user"></i>
              </span>
              <span class="title">Students</span>
            </a>
          </li>
          <li class="nav-item dropdown">
            <a class="sidebar-link" href="{%url 'manage-grades'%}">
              <span class="icon-holder">
                <i class="c-pink-500 ti-palette"></i>
              </span>
              <span class="title">Manage grades</span>
            </a>
          </li>
          <li class="nav-item dropdown">
            <a class="sidebar-link" href="{%url 'enrollSelection'%}">
              <span class="icon-holder">
                <i class="c-orange-500 ti-layout-list-thumb"></i>
              </span>
              <span class="title">Student by Course</span>
            </a>
          </li>

          <li class="nav-item dropdown">
            <a class="dropdown-toggle" href="javascript:void(0);">
              <span class="icon-holder">
                <i class="c-red-500 ti-files"></i>
              </span>
              <span class="title">Enroll Student</span>
              <span class="arrow">
                <i class="ti-angle-right"></i>
              </span>
            </a>
            <ul class="dropdown-menu">
              <li>
                <a class="sidebar-link" href="{%url 'addNewStudentAPI'%}">
                  <span class="icon-holder">
                    <i class="c-red-500 ti-user"></i>
                  </span>
                  <span class="title">Enroll as New Student</span>
                </a>
              </li>
              <li>
                <a class="sidebar-link" href="{%url 'checkMyEnrollment'%}">
                  <span class="icon-holder">
                    <i class="c-cyan-500 ti-user"></i>
                  </span>
                  <span class="title">Enroll as Old Student</span>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="sidebar-link" href="{%url 'checkMyEnrollment'%}">
              <span class="icon-holder">
                <i class="c-light-blue-500 ti-eye"></i>
              </span>
              <span class="title">View My Enrollment</span>
            </a>
          </li>
        </ul>
      </div>
    </div>

    <!-- #Main ============================ -->
    <div class="page-container">
      <!-- ### $Topbar ### -->
      <div class="header navbar">
        <div class="header-container">
          <ul class="nav-left">
            <li>
              <a
                id="sidebar-toggle"
                class="sidebar-toggle"
                href="javascript:void(0);"
              >
                <i class="ti-menu"></i>
              </a>
            </li>
            <li class="search-box">
              <a class="search-toggle no-pdd-right" href="javascript:void(0);">
                <i class="search-icon ti-search pdd-right-10"></i>
                <i class="search-icon-close ti-close pdd-right-10"></i>
              </a>
            </li>
            <li class="search-input">
              <input class="form-control" type="text" placeholder="Search..." />
            </li>
          </ul>

          <ul class="nav-right">
            <li class="notifications dropdown">
              <span class="counter bgc-red">3</span>
              <a
                href=""
                class="dropdown-toggle no-after"
                data-toggle="dropdown"
              >
                <i class="ti-bell"></i>
              </a>

              <ul class="dropdown-menu">
                <li class="pX-20 pY-15 bdB">
                  <i class="ti-bell pR-10"></i>
                  <span class="fsz-sm fw-600 c-grey-900">Notifications</span>
                </li>

                <li>
                  <!-- <ul
                      style="max-height: 300px;"
                      class="ovY-a pos-r scrollable lis-n p-0 m-0 fsz-sm"
                    >
                      {%for f in forwarded%}
                      <li>
                        <a
                          href="{%url 'enrollDetailsAdmin' f.pk %}"
                          class="peers fxw-nw td-n p-20 bdB c-grey-800 cH-blue bgcH-grey-100"
                        >
                          <div class="peer mR-15">
                            <img
                              class="w-3r bdrs-50p"
                              src="{% static 'student_profile/assets/images/faces/face10.jpg'%}"
                              alt=""
                            />
                          </div>
                          <div class="peer peer-greed">
                            <span>
                              <span class="fw-500"
                                >{{f.student.last_name}},
                                {{f.student.first_name}}
                              </span>
                              <span class="c-grey-600"
                                >is forwarded
                                <span class="text-dark">enrollment</span>
                              </span>
                            </span>
                            <p class="m-0">
                              <small class="fsz-xs">5 mins ago</small>
                            </p>
                          </div>
                        </a>
                      </li>
                      {%endfor%}
                    </ul> -->
                </li>

                <li class="pX-20 pY-15 ta-c bdT">
                  <span>
                    <a href="" class="c-grey-600 cH-blue fsz-sm td-n"
                      >View All Notifications
                      <i class="ti-angle-right fsz-xs mL-10"></i
                    ></a>
                  </span>
                </li>
              </ul>
            </li>

            <li class="dropdown">
              <a
                href=""
                class="dropdown-toggle no-after peers fxw-nw ai-c lh-1"
                data-toggle="dropdown"
              >
                <div class="peer mR-10">
                  <img
                    class="w-2r bdrs-50p"
                    src="{% static 'student_profile/images/admin.jpg' %}"
                    alt=""
                  />
                </div>
                <div class="peer">
                  <!-- <span class="fsz-sm c-grey-900"
                      >{{request.user.username}}</span
                    > -->
                </div>
              </a>
              <ul class="dropdown-menu fsz-sm">
                <li>
                  <a href="" class="d-b td-n pY-5 bgcH-grey-100 c-grey-700">
                    <i class="ti-settings mR-10"></i>
                    <span>Setting</span>
                  </a>
                </li>
                <li>
                  <a href="" class="d-b td-n pY-5 bgcH-grey-100 c-grey-700">
                    <i class="ti-user mR-10"></i>
                    <span>Profile</span>
                  </a>
                </li>

                <li role="separator" class="divider"></li>
                <li>
                  <a
                    href="{%url 'logout'%}"
                    class="d-b td-n pY-5 bgcH-grey-100 c-grey-700"
                  >
                    <i class="ti-power-off mR-10"></i>
                    <span>Logout</span>
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>

      <!-- ### $App Screen Content ### -->
      <main class="main-content bgc-grey-100">
        <div id="mainContent">
          <div class="full-container">
            <router-view></router-view>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<style>
#loader {
  transition: all 0.3s ease-in-out;
  opacity: 1;
  visibility: visible;
  position: fixed;
  height: 100vh;
  width: 100%;
  background: #fff;
  z-index: 90000;
}

#loader.fadeOut {
  opacity: 0;
  visibility: hidden;
}

.spinner {
  width: 40px;
  height: 40px;
  position: absolute;
  top: calc(50% - 20px);
  left: calc(50% - 20px);
  background-color: #333;
  border-radius: 100%;
  -webkit-animation: sk-scaleout 1s infinite ease-in-out;
  animation: sk-scaleout 1s infinite ease-in-out;
}

@-webkit-keyframes sk-scaleout {
  0% {
    -webkit-transform: scale(0);
  }

  100% {
    -webkit-transform: scale(1);
    opacity: 0;
  }
}

@keyframes sk-scaleout {
  0% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  100% {
    -webkit-transform: scale(1);
    transform: scale(1);
    opacity: 0;
  }
}
</style>

<script>
/* eslint-disable */
export default {
  name: "AdminitorDash",
};
</script>

<style></style>
