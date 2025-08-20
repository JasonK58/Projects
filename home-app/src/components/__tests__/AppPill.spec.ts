import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import AppPill from "../AppPill.vue";

describe("AppPill", () => {
  const title = "title";
  const url = "url";

  it("renders fields", () => {
    const wrapper = mount(AppPill, {
      props: { title: title, url: url },
    });
    const link = wrapper.find("a");

    expect(link.text()).toContain(title);
    expect(link.attributes("href")).toBe(url);
  });
});
