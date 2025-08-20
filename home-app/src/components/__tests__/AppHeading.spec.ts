import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import AppHeading from "../AppHeading.vue";

describe("AppHeading", () => {
  const title = "title";

  it("renders fields", () => {
    const wrapper = mount(AppHeading, {
      props: { title: title },
    });
    expect(wrapper.text()).toContain(title);
  });
});
