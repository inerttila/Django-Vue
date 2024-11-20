<script setup>
import ReviewCard from './components/ReviewCard.vue'
import 'vue3-toastify/dist/index.css'

import { onMounted } from 'vue'
import { useGeneralsStore } from './stores/generals'
import { storeToRefs } from 'pinia'

const generalsStore = useGeneralsStore()
const { reviewsList, filteredReviews } = storeToRefs(generalsStore)

const fetchAndSetReviews = async () => {
  try {
    const res = await fetch('http://192.168.40.14:8000/api/reviews/')

    const reviews = await res.json()

    reviewsList.value = reviews
    filteredReviews.value = reviews
  } catch (error) {
    console.log(error)
  }
}

onMounted(async () => {
  // console.log('Component is mounted!')
  fetchAndSetReviews()
})

const refetchReviews = () => {
  fetchAndSetReviews()
}
</script>

<template>
  <div class="custom-template-body">
    <div class="bg"></div>
    <div class="mask"></div>
    <h1 class="slogan">The Future Of Possible</h1>
  </div>
  <ReviewCard msg="You did it" :reviewsList="reviewsList" :refetchReviews="refetchReviews" />
</template>

<style scoped></style>
