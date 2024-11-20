<script setup>
import ReView from './ReView.vue'
import NewReviewForm from './NewReviewForm.vue'
import { MagnifyingGlassIcon } from '@heroicons/vue/24/solid'
import { useGeneralsStore } from '../stores/generals'
import { storeToRefs } from 'pinia'
import { ref } from 'vue'

const generalsStore = useGeneralsStore()
const { showNewReviewForm, reviewsList, filteredReviews } = storeToRefs(generalsStore)

const searchInput = ref('')

defineProps({
  msg: {
    type: String,
    required: true
  },
  refetchReviews: {
    type: Function,
    required: true
  }
})

const handleSearch = () => {
  const filtered = reviewsList.value.filter((review) => {
    return (
      review.review.toLowerCase().includes(searchInput.value.toLowerCase()) ||
      review.userName.toLowerCase().includes(searchInput.value.toLowerCase())
    )
  })

  filteredReviews.value = filtered
}
</script>

<template>
  <div class="greetings max-w-7xl mx-auto px-4">
    <div class="flex flex-col justify-center items-center min-h-screen space-y-6">
      <div
        class="flex flex-col lg:flex-row justify-center items-center w-full space-y-4 lg:space-y-0"
      >
        <div
          class="flex items-center border border-white rounded-md shadow-sm w-full max-w-md lg:max-w-xs overflow-hidden"
          v-if="reviewsList.length"
        >
          <MagnifyingGlassIcon class="p-3 w-10 h-10 text-gray" />
          <input
            type="text"
            placeholder="Search Product"
            class="p-2 w-full bg-transparent text-white focus:outline-none"
            v-model="searchInput"
            @keyup="handleSearch"
          />
        </div>

        <button
          class="py-2 px-8 bg-gradient-to-r text-white text-lg rounded-lg shadow-lg border border-white focus:outline-none transition-transform transform hover:scale-105 lg:ml-4"
          @click="showNewReviewForm = !showNewReviewForm"
        >
          {{ showNewReviewForm ? 'Cancel' : 'Add Product' }}
        </button>
      </div>

      <div v-if="showNewReviewForm" class="w-full max-w-xl">
        <NewReviewForm :refetchReviews="refetchReviews" :showNewReviewForm="showNewReviewForm" />
      </div>

      <ul class="flex flex-wrap justify-center gap-6 my-10">
        <li
          v-for="review in filteredReviews"
          :key="review.id"
          class="w-full sm:w-72 rounded-lg shadow-lg bg-transparent border border-gray-200 p-4 transition-transform transform hover:scale-105"
        >
          <ReView :review="review" />
        </li>
      </ul>
    </div>
  </div>
</template>
