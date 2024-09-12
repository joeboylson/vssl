import { useState } from "react";

export function useToggle(defaultValue?: boolean) {
  const [value, setValue] = useState<boolean>(defaultValue ?? false);
  const enable = () => setValue(true);
  const disable = () => setValue(false);
  const toggle = () => (value ? disable() : enable());
  return { value, enable, disable, toggle };
}
