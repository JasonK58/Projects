import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import DropdownMenu from '@/components/dropdownMenu.vue'

describe('DropdownMenu', () => {
  const placeholderOption: string = 'Select an option'
  const options: string[] = ['a', 'b', 'c']

  it('renders placeholder text', () => {
    const wrapper = mount(DropdownMenu, {
      props: { placeholderOption: placeholderOption, options: options },
    })
    const placeholderElement = wrapper.find('option')
    expect(placeholderElement.element.text).toEqual(placeholderOption)
    expect(placeholderElement.element.value).toEqual('')
  })

  it('renders options, no placeholder provided', () => {
    const wrapper = mount(DropdownMenu, { props: { options: options } })
    const optionsList = wrapper.findAll('option')
    optionsList.forEach((option) => {
      expect(option.element.value).toBeOneOf(options)
    })
    expect(optionsList.length).toEqual(options.length)
  })

  it('renders options, placeholder provided', () => {
    const wrapper = mount(DropdownMenu, {
      props: { placeholderOption: placeholderOption, options: options },
    })
    const optionsList = wrapper.findAll('option')
    optionsList.shift() // Remove the placeholder text that the dropdown adds as an option.
    expect(optionsList.length).toEqual(options.length)
    optionsList.forEach((option) => {
      expect(option.element.value).toBeOneOf(options)
    })
  })
})
