import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import WritingPromptGenerator from '../WritingPromptGenerator.vue'

describe('WritingPromptGenerator', () => {
  it('renders properly', () => {
    const wrapper = mount(WritingPromptGenerator, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
})
