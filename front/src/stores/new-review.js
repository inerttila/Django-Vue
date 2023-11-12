import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useNewReviewStore = defineStore('newReview', () => {
  const userNameInput = ref('')
  const reviewInput = ref('')
  const optionsInput = ref('default')
  const thumbsUpCount = ref(0)
  const thumbsDownCount = ref(0)

  function incrementThumbsUp() {
    thumbsUpCount.value++
  }

  function incrementThumbsDown() {
    thumbsDownCount.value++
  }

  function updateUserNameInput(newUserName) {
    userNameInput.value = newUserName
  }

  function updateReviewInput(newReview) {
    reviewInput.value = newReview
  }

  function updateOptionsInput(newOptions) {
    optionsInput.value = newOptions
  }

  return {
    userNameInput,
    reviewInput,
    optionsInput,
    thumbsUpCount,
    thumbsDownCount,
    incrementThumbsUp,
    incrementThumbsDown,
    updateUserNameInput,
    updateReviewInput,
    updateOptionsInput
  }
})
