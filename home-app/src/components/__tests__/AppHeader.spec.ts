import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import AppHeader from "../AppHeader.vue";

describe("AppHeader", () => {
  const name = "name";
  const title = "title";
  const location = "location";

  it("renders fields", () => {
    const wrapper = mount(AppHeader, {
      props: { name: name, title: title, location: location },
    });
    expect(wrapper.text()).toContain(name);
    expect(wrapper.text()).toContain(title);
    expect(wrapper.text()).toContain(location);
  });

  it("renders image", () => {
    const wrapper = mount(AppHeader, {
      props: { name: name, title: title, location: location },
    });
    const image = wrapper.find("img");
    expect(image.exists()).toBe(true);
  });
});
