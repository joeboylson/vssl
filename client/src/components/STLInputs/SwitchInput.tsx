import { ChangeEvent, useCallback } from "react";
import { Switch } from "@mui/material";
import styled from "styled-components";

const INPUT_SPACING_LEFT = 12;

const StyledSwitchInput = styled.div`
  width: calc(100% - ${INPUT_SPACING_LEFT * 2}px);
  margin-left: ${INPUT_SPACING_LEFT}px;
  padding-left: ${INPUT_SPACING_LEFT}px;

  display: grid;
  grid-template-columns: repeat(2, 1fr);
  align-items: center;
  border-radius: 4px;
  border: 1px solid #ccc;

  .MuiFormControl-root {
    width: 100%;
  }

  * {
    font-family: Elios !important;
  }
`;

interface _props {
  label: string;
  onChange: (value: boolean) => void;
  defaultValue?: boolean;
}

export function SwitchInput({ label, onChange, defaultValue = false }: _props) {
  const _onChange = useCallback(
    (event: ChangeEvent<HTMLInputElement>) => {
      const value = event.target.checked;
      onChange(value);
    },
    [onChange]
  );

  return (
    <StyledSwitchInput>
      <p>{label}</p>
      <Switch defaultChecked={defaultValue} onChange={_onChange} />
    </StyledSwitchInput>
  );
}
