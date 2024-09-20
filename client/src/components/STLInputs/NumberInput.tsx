import { ChangeEvent, useCallback, useMemo } from "react";
import { MAX_BED_SIZE } from "../../constants";
import { TextField } from "@mui/material";
import { inRange } from "lodash";
import styled from "styled-components";

const INPUT_SPACING_LEFT = 12;

const StyledNumberInput = styled.div`
  width: calc(100% - ${INPUT_SPACING_LEFT}px);
  padding-left: ${INPUT_SPACING_LEFT}px;

  .MuiFormControl-root {
    width: 100%;
  }

  * {
    font-family: Elios !important;
  }
`;

interface _props {
  label: string;
  onChange: (value: number) => void;
  defaultValue?: number;
  min?: number;
  max?: number;
}

export function NumberInput({
  label,
  onChange,
  defaultValue = 1,
  min = 1,
  max = MAX_BED_SIZE,
}: _props) {
  const _onChange = useCallback(
    (event: ChangeEvent<HTMLInputElement>) => {
      const value = Number(event.target.value);
      onChange(value);
    },
    [onChange]
  );

  const errorMessage = useMemo(() => {
    if (!inRange(defaultValue, min, max + 1)) {
      return "Out of range";
    }
  }, [defaultValue, min, max]);

  return (
    <StyledNumberInput>
      <TextField
        error={!!errorMessage}
        helperText={errorMessage}
        label={`${label}: [min: ${min}, max:${max}]`}
        type="number"
        InputProps={{ inputProps: { min, max } }}
        onChange={_onChange}
        defaultValue={defaultValue}
        size="small"
      />
    </StyledNumberInput>
  );
}
