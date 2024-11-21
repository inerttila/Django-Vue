<script setup>
import { ShoppingCartIcon, XMarkIcon } from '@heroicons/vue/24/solid'
import { ref, h } from 'vue'
import { toast } from 'vue3-toastify'

defineProps({
  review: {
    type: Object,
    required: true
  }
})

const votedThumb = ref('')

const updateLikeCount = async (review) => {
  const res = await fetch(
    `http://192.168.40.14:8000/api/reviews/${review.id}/update_thumbs_count/`,
    {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        thumbsUppCount: review.thumbsUppCount,
        thumbsDownCount: review.thumbsDownCount
      })
    }
  )

  if (!res.ok) {
    toast.error('Something went wrong!')
    return
  }

  toast.success('Thanks for Checking!', {
    style: {
      fontSize: '12px',
      maxWidth: '200px',
      borderRadius: '8px'
    },
    position: 'top-right'
  })
}

const onThumbUp = async (review) => {
  const toastId = toast.info(
    h('div', [
      h('p', 'Are you sure you got this product?'),
      h('div', { class: 'flex gap-2 mt-2' }, [
        h(
          'button',
          {
            class: 'px-4 py-2 bg-blue-500 text-white rounded-md',
            onClick: () => handleThumbUp(review, toastId)
          },
          'Yes'
        ),
        h(
          'button',
          {
            class: 'px-4 py-2 bg-gray-300 text-black rounded-md',
            onClick: () => handleCancel(toastId)
          },
          'No'
        )
      ])
    ]),
    {
      autoClose: false,
      position: 'top-right',
      closeButton: false,
      hideProgressBar: true,
      style: {
        fontSize: '12px',
        maxWidth: '200px',
        borderRadius: '8px'
      }
    }
  )
}

const onThumbDown = async (review) => {
  const toastId = toast.info(
    h('div', [
      h('p', 'Are you sure you sold this product?'),
      h('div', { class: 'flex gap-2 mt-2' }, [
        h(
          'button',
          {
            class: 'px-4 py-2 bg-blue-500 text-white rounded-md',
            onClick: () => handleThumbDown(review, toastId)
          },
          'Yes'
        ),
        h(
          'button',
          {
            class: 'px-4 py-2 bg-gray-300 text-black rounded-md',
            onClick: () => handleCancel(toastId)
          },
          'No'
        )
      ])
    ]),
    {
      autoClose: false,
      position: 'top-right',
      closeButton: false,
      hideProgressBar: true,
      style: {
        fontSize: '12px',
        maxWidth: '200px',
        borderRadius: '8px'
      }
    }
  )
}

const handleThumbUp = async (review, toastId) => {
  votedThumb.value = 'up'
  review.thumbsUppCount += 1
  await updateLikeCount(review)
  toast.remove(toastId) // Remove the specific toast using its ID
}

const handleThumbDown = async (review, toastId) => {
  votedThumb.value = 'down'
  review.thumbsDownCount += 1
  await updateLikeCount(review)
  toast.remove(toastId) // Remove the specific toast using its ID
}

const handleCancel = (toastId) => {
  toast.remove(toastId) // Remove the specific toast if the user clicks 'No'
}
</script>

<template>
  <div class="flex flex-col gap-4 p-4 w-full h-full rounded-md">
    <div class="flex justify justify-between">
      <div class="flex gap-2">
        <div class="w-7 h-7 text-center rounded-full bg-blue-950">
          {{ review.userName.charAt(0) }}
        </div>
        <span>{{ review.userName }}</span>
      </div>
      <div class="flex p-1 gap-1 text-orange-300"></div>
    </div>

    <div>{{ review.review }}</div>

    <div class="flex justify-between">
      <span>{{ new Date(review.created_at).toLocaleDateString() }}</span>

      <div class="flex gap-2">
        <div class="flex cursor-pointer" @click="() => onThumbUp(review)">
          <ShoppingCartIcon
            class="h-6 w-5"
            :class="votedThumb === 'up' ? 'text-blue-500' : 'text-gray-100'"
          />
          {{ review.thumbsUppCount }}
        </div>

        <div class="flex cursor-pointer" @click="() => onThumbDown(review)">
          <XMarkIcon
            class="h-6 w-5"
            :class="votedThumb === 'down' ? 'text-blue-500' : 'text-gray-100'"
          />
          {{ review.thumbsDownCount }}
        </div>
      </div>
    </div>
  </div>
</template>
