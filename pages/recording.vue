<template>
    <div class="relative z-10 max-w-screen-sm">
      <p v-if="user" class="fVeafc in">Hi, {{ user.user_metadata.first_name }}</p>
      <p v-else class="fVeafc">unauthenticated</p>

      <div class="relative z-10 max-w-screen-sm">
    <!-- Existing content -->
    
    <div v-if="user" class="audio-recorder-wrapper">
      <audio-recorder
        :upload-url="'your-upload-url'"
        :headers="{ Authorization: 'Bearer your_access_token' }"
        @successful-upload="handleSuccess"
        @failed-upload="handleFailure"
      />
    </div>
    
    <!-- Remaining template content -->
  </div>

      </div>
    
  </template>
  
  <script setup lang="ts">
  import { defineComponent, ref } from 'vue';
  import Recorder from 'js-audio-recorder'

  import Vue from 'vue';

import AudioRecorder from 'vue-audio-recorder';

const client = useSupabaseAuthClient();
const user = useSupabaseUser();
const loading = ref(false);

const handleSuccess = (response) => {
  console.log('Upload successful:', response);
};

const handleFailure = (error) => {
  console.error('Upload failed:', error);
};


  const logout = async () => {
    loading.value = true
    const { error } = await client.auth.signOut()
    if (error) {
      loading.value = false
      return alert('Something went wrong !')
    }
  }
  
  useHead({
    title: 'Login',
    meta: [
      { name: 'description', content: 'You can use our translation software to convert multiple dialects to Mandarin, and also learn and practice on our platform. We also provide AI based exam scoring functions.' }
    ]
  })
  </script>
  