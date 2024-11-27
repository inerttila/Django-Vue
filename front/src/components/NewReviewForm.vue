<script setup>
import { ref } from 'vue'
import { toast } from 'vue3-toastify'

import { useNewReviewStore } from '../stores/new-review'
import { storeToRefs } from 'pinia'
import { useGeneralsStore } from '../stores/generals'

const newReviewStore = useNewReviewStore()
const generalsStore = useGeneralsStore()
const { showNewReviewForm } = storeToRefs(generalsStore)

const { userNameInput, reviewInput, optionsInput, thumbsUpCount, thumbsDownCount } =
  storeToRefs(newReviewStore)
const { updateUserNameInput, updateReviewInput, updateOptionsInput } = newReviewStore

const noOptionsSelectedMsg = ref('')

defineProps({
  review: {
    type: Object,
    required: true
  },
  refetchReviews: {
    type: Function,
    required: true
  }
})

const handleSubmit = async (e, refetch) => {
  e.preventDefault()

  // if no options selected, return
  if (optionsInput.value === 'default') {
    noOptionsSelectedMsg.value = 'Please select an option'
    return
  }

  try {
    const dataObj = {
      userName: userNameInput.value || 'Anonymous',
      thumbsUppCount: thumbsUpCount.value,
      thumbsDownCount: thumbsDownCount.value,
      review: reviewInput.value,
      shop: optionsInput.value
    }

    const res = await fetch('http://192.168.40.14:8000/api/reviews/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dataObj)
    })
    if (!res.ok) {
      throw new Error('There was an error adding this product')
    }

    // clear inputs
    updateUserNameInput('')
    updateReviewInput('')
    updateOptionsInput('default')

    // show toast
    toast.success('Product added successfully', {
      style: {
        fontSize: '12px',
        maxWidth: '200px',
        borderRadius: '8px'
      },
      position: 'top-right'
    })

    // refetch reviews
    refetch()

    // hide form
    showNewReviewForm.value = false
  } catch (error) {
    console.log('error', error)
  }
}
</script>

<template>
  <div class="flex min-h-full flex-col justify-center px-6 lg:px-8">
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit="handleSubmit($event, refetchReviews)">
        <div>
          <label for="username" class="block text-sm font-medium leading-6">Product Name</label>
          <div class="mt-2">
            <input
              id="username"
              name="username"
              type="text"
              autocomplete="username"
              placeholder="Product Name"
              class="block text-black w-full ps-2 rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="userNameInput"
            />
          </div>
        </div>

        <div>
          <label for="options" class="block text-sm font-medium leading-6">Shop</label>
          <div class="mt-2">
            <select
              id="options"
              name="options"
              autocomplete="options"
              required
              class="block text-black w-full ps-2 rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="optionsInput"
            >
              <option value="default" disabled>Select the Shop</option>
              <option value="skaitech">SKAITECH</option>
              <option value="3dskai">3DSKAI</option>
            </select>
            {{ noOptionsSelectedMsg }}
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="review" class="block text-sm font-medium leading-6">Price</label>
          </div>
          <div class="mt-2">
            <textarea
              id="review"
              name="review"
              type="text"
              autocomplete="review"
              placeholder="Price and Description"
              required
              class="block text-black w-full ps-2 rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="reviewInput"
            ></textarea>
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
