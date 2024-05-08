<template>
    <div class="relative z-10 max-w-screen-sm">
      <p v-if="user" class="fVeafc in">Hi, {{ user.user_metadata.first_name }}</p>
      <p v-else class="fVeafc">unauthenticated</p>
      <h1 class="kKxhrq">
        Exam
      </h1>
      <p class="kRTmDC">
        In this section, you can practice Cantonese in real-life conversation scenarios and receive ratings based on our independently developed AI model. Through this, you can effectively improve your dialect level.
      </p>
      <div class="uQxNj" v-if="user">
        <div>
        <NuxtLink to="/exam1">
          <button class="ieMfVH">
            <span class="fKlELC">
              Phrase Exam
            </span>
          </button>
        </NuxtLink>
    </div>
    <div>
        <NuxtLink to="/exam2">
          <button class="ieMfVH">
            <span class="fKlELC">
              Sentence Exam
            </span>
          </button>
        </NuxtLink>
    </div>
        
      </div>
      <div class="uQxNj" v-else>
        <NuxtLink class="bQRHNT" to="/login">
          <span class="fKlELC">
            Login 
            <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="taKtSf">
              <path class="chevron" d="M8 13L13 8L8 3" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="round"></path>
              <path class="stem" d="M12 8L2 8" stroke-width="1.5"></path>
            </svg>
          </span>
        </NuxtLink>
        <NuxtLink to="/register">
          <button class="ieMfVH">
            <span class="fKlELC">
              Sign up
            </span>
          </button>
        </NuxtLink>
      </div>
      <br><br><br><br>
      <div>
        <NuxtLink to="/home">
          <button class="ieMfVH">
            <span class="fKlELC">
              Back
            </span>
          </button>
        </NuxtLink>
    </div>
    </div>
  </template>
  
  <script setup lang="ts">
  const client = useSupabaseAuthClient()
  const user = useSupabaseUser()
  const loading = ref(false)
  
  const logout = async () => {
    loading.value = true
    const { error } = await client.auth.signOut()
    if (error) {
      loading.value = false
      return alert('Something went wrong !')
    }s
  }
  
  useHead({
    title: 'Exam',
    meta: [
      { name: 'description', content: 'In this section, you can practice Cantonese in real-life conversation scenarios and receive ratings based on our independently developed AI model. Through this, you can effectively improve your dialect level.' }
    ]
  })
  </script>
  