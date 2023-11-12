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
  <div class="greetings max-w-7xl m-auto">
    <div class="flex justify-center items-center min-h-screen">
      <div class="flex flex-col gap-2 p-5">
        <div class="flex justify-between items-center gap-32">
          <h1 class="text-lg" v-if="reviewsList.length === 0">Add First Review</h1>
          <h1 class="text-lg" v-else>Reviews</h1>
          <div
            class="flex bg-gray-600 bg-opacity-20 border border-gray-200 rounded-md"
            v-if="reviewsList.length"
          >
            <MagnifyingGlassIcon class="py-4 p-3 w-16 h-16" />
            <input
              type="email"
              name="email"
              id="email"
              placeholder="Search Review"
              class="p-2 bg-transparent focus:outline-none"
              v-model="searchInput"
              @keyup="handleSearch"
            />
          </div>
        </div>

        <div class="flex justify-center">
          <button
            class="mt-10 p-2 px-4 bg-gray-900 hover:bg-gray-950 border border-gray-950 bg-opacity-60 text-white"
            @click="showNewReviewForm = !showNewReviewForm"
          >
            {{ showNewReviewForm ? 'Cancel' : 'Add Review' }}
          </button>
        </div>

        <div v-if="showNewReviewForm">
          <NewReviewForm :refetchReviews="refetchReviews" :showNewReviewForm="showNewReviewForm" />
        </div>

        <!-- Item Container -->
        <ul class="flex flex-wrap justify-center gap-4 my-14">
          <li v-for="review in filteredReviews" :key="review.id" class="max-w-xs w-full rounded-md">
            <ReView :review="review" />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
