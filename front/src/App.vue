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
    const res = await fetch('http://localhost:8000/api/reviews/')

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
  <ReviewCard msg="You did it" :reviewsList="reviewsList" :refetchReviews="refetchReviews" />
</template>

<style scoped></style>
