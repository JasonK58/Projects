import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import AppList from "../AppList.vue";

describe("AppPill", () => {
  const listValues = ["foo", "bar"];

  it("renders values", () => {
    const wrapper = mount(AppList, {
      props: { listValues: listValues },
    });
    listValues.forEach((value) => {
      expect(wrapper.text()).toContain(value);
    });
  });
});
