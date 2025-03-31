import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'

describe('AppHeader', () => {
  const msg = 'message'
  it('renders message', () => {
    const wrapper = mount(AppHeader, { props: { msg: msg, logo: Logo } })
    expect(wrapper.text()).toContain(msg)
  })

  it('renders image', () => {
    const wrapper = mount(AppHeader, { props: { msg: msg, logo: Logo } })
    const image = wrapper.find('img')
    expect(image.exists()).toBe(true)
  })

  it('renders no image if not provided', () => {
    const wrapper = mount(AppHeader, { props: { msg: msg } })
    const image = wrapper.find('img')
    expect(image.exists()).toBe(false)
  })
})
