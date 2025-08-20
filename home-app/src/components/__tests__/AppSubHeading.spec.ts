import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import AppSubHeading from "../AppSubHeading.vue";

describe("AppSubHeading", () => {
  const title = "title";

  it("renders fields", () => {
    const wrapper = mount(AppSubHeading, {
      props: { title: title },
    });
    expect(wrapper.text()).toContain(title);
  });
});
