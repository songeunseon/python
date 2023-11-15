<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <h3 class="navbar-brand"><b>안녕하세요</b></h3>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Main</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Lotto
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">랜던번호</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">회차결과</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="회차(숫자)만 입력해주세요" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">확인</button>
      </form>
    </div>
  </div>
</nav>
  <RouterView />
</template>

<style scoped>

</style>
