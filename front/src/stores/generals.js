import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useGeneralsStore = defineStore('generals', () => {
  const showNewReviewForm = ref(false)
  const reviewsList = ref([])
  console.log('reviewsList', reviewsList)
  const filteredReviews = ref([])

  function toggleShowNewReviewForm() {
    showNewReviewForm.value = !showNewReviewForm.value
  }

  return {
    showNewReviewForm,
    toggleShowNewReviewForm,
    reviewsList,
    filteredReviews
  }
})
